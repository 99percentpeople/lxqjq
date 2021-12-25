import math

import numpy as np

材料类型表 = ["梁单元"]
结点类型表 = ["固定支座", "铰支座", "刚接", "铰接"]
分布力类型表 = ["分布横向力"]
集中力类型表 = ["整体X方向力", "整体Y方向力", "弯矩"]

class 材料:
    def __init__(self, _类型: str, _刚度:  float, _静矩:  float, _横截面积: float):
        self.类型 = _类型
        self.刚度 = float(_刚度)
        self.静矩 = float(_静矩)
        self.横截面积=float(_横截面积)

    def __eq__(self, other):
        match other:
            case int():
                return self.编号 == other
            case 材料():
                return self.编号 == other.编号
            case _:
                raise ValueError(f"{type(other)} 为不允许的类型")

    def __str__(self):
        return str(self.编号)


class 分布力:
    def __init__(self, _单元编号: int, _类型: str, _Q1:  float, _Q2:  float):
        self.单元编号 = int(_单元编号)
        self.类型 = _类型
        self.Q1 = float(_Q1)
        self.Q2 = float(_Q2)

    def __eq__(self, other):
        match other:
            case int():
                return self.编号 == other
            case 分布力():
                if self.类型 == other.类型:
                    return True
            case _:
                raise ValueError(f"{type(other)} 为不允许的类型")

        return False

    def __str__(self):
        return str(self.编号)


class 集中力:
    def __init__(self, _结点编号, _类型: str, _F:  float):
        self.结点编号 = int(_结点编号)
        self.类型 = _类型
        self.F = float(_F)

    def __eq__(self, other):
        match other:
            case int():
                return self.编号 == other
            case 集中力():
                if self.类型 == other.类型:
                    return True
            case _:
                raise ValueError(f"{type(other)} 为不允许的类型")

        return False

    def __str__(self):
        return str(self.编号)


class 位移:
    def __init__(self, _结点编号: int, _UX:  float, _UY:  float, _Φ:  float):
        self.结点编号 = int(_结点编号)
        self.UX = float(_UX)
        self.UY = float(_UY)
        self.Φ = float(_Φ)

    def 清空(self):
        self.UX = 0.
        self.UY = 0.
        self.Φ = 0.


class 结点:
    def __init__(self, _X坐标:  float, _Y坐标:  float, _约束类型: str):
        self.X坐标 = float(_X坐标)
        self.Y坐标 = float(_Y坐标)
        self.约束类型 = _约束类型
        self.集中力表 = []

    def __eq__(self, other):
        match other:
            case int():
                return self.编号 == other
            case 结点():
                return self.编号 == other.编号
            case _:
                raise ValueError(f"{type(other)} 为不允许的类型")

    def __str__(self):
        return str(self.编号)

    def 添加集中力(self, _集中力: 集中力):
        try:
            self.集中力表.index(_集中力)
        except ValueError:
            self.集中力表.append(_集中力)
        else:
            raise ValueError("该集中力已存在")

    def 修改集中力(self, _集中力: 集中力, 编号: int):
        try:
            self.集中力表[self.集中力表.index(编号)] = _集中力
        except ValueError:
            raise ValueError("集中力不存在")

    def 删除集中力(self, 编号: int):
        try:
            self.集中力表.remove(编号)
        except ValueError:
            raise ValueError("集中力不存在")


class 耦合结点:
    def __init__(self, _结点1: 结点, _结点2: 结点, _自由度: int):
        pass


class 单元:
    def __init__(self, _结点1: 结点, _结点2: 结点, _材料: 材料):
        if _结点1 == _结点2:
            raise ValueError("不能以相同结点创建一个单元")
        self.结点1 = _结点1
        self.结点2 = _结点2
        self.材料 = _材料
        self.分布力表 = []
        
        self.计算属性()

    def __eq__(self, other):
        match other:
            case int():
                return self.编号 == other
            case 单元():
                if self.结点1 == other.结点1 and self.结点2 == other.结点2:
                    return True
                if self.结点1 == other.结点2 and self.结点2 == other.结点1:
                    return True
            case 结点():
                return self.结点1 == other.编号 or self.结点2 == other.编号
            case _:
                raise ValueError(f"{type(other)} 为不允许的类型")
        return False

    def __str__(self):
        return str(self.编号)
    
    def __getattr__(self, name):
        match name:
            case "坐标变换矩阵":
                return self.计算坐标变换矩阵()
            case "总体单刚":
                return self.计算单元刚度矩阵()
            case "整体固端力":
                return self.计算结点固端力()
            
    
    def 修改结点(self,_结点:结点):
        if self.结点1 == _结点:
            self.结点1 = _结点
        elif self.结点2 == _结点:
            self.结点2 = _结点
            
    def 添加分布力(self, _分布力: 分布力):
        try:
            self.分布力表.index(_分布力)
        except ValueError:
            self.分布力表.append(_分布力)
            self.计算结点荷载()
        else:
            raise ValueError("该分布力已存在")

    def 修改分布力(self, _分布力: 分布力, 编号: int):
        try:
            self.分布力表[self.分布力表.index(编号)] = _分布力  
            self.计算结点荷载()
        except ValueError:
            raise ValueError("分布力不存在")
        

    def 删除分布力(self, 编号: int):
        try:
            self.分布力表.remove(编号)
        except ValueError:
            raise ValueError("分布力不存在")

    def 计算属性(self):
        self.l = math.sqrt((
            (self.结点1.X坐标-self.结点2.X坐标) ** 2. +
            (self.结点1.Y坐标-self.结点2.Y坐标) ** 2.))

        self.i = (self.材料.刚度*self.材料.静矩)/self.l

        self.sinA = (self.结点2.Y坐标-self.结点1.Y坐标)/self.l
        self.cosA = (self.结点2.X坐标-self.结点1.X坐标)/self.l
        # logging.debug(f"l = {self.l}; i = {self.i}; sinA = {self.sinA}; cosA = {self.cosA}")

    def 计算坐标变换矩阵(self):
        坐标变换矩阵 = \
            np.array([[self.cosA, self.sinA, 0, 0, 0, 0],
                      [-self.sinA, self.cosA, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [0, 0, 0, self.cosA, self.sinA, 0],
                      [0, 0, 0, -self.sinA, self.cosA, 0],
                      [0, 0, 0, 0, 0, 1]])
        return 坐标变换矩阵

    def 计算单元刚度矩阵(self):
        _EA_L = (self.材料.刚度*self.材料.横截面积)/self.材料.静矩
        _2EI_L = (2*self.材料.刚度*self.材料.静矩)/self.l
        _4EI_L = (4*self.材料.刚度*self.材料.静矩)/self.l
        _6EI_L2 = (6*self.材料.刚度*self.材料.静矩)/self.l**2
        _12EI_L3 = (12*self.材料.刚度*self.材料.静矩)/self.l**3

        局部单刚 = \
            np.array([[_EA_L, 0, 0, -_EA_L, 0, 0],
                      [0, _12EI_L3, _6EI_L2, 0, -_12EI_L3, _6EI_L2],
                      [0, _6EI_L2, _4EI_L, 0, -_6EI_L2, _2EI_L],
                      [-_EA_L, 0, 0, _EA_L, 0, 0],
                      [0, -_12EI_L3, -_6EI_L2, 0, _12EI_L3, -_6EI_L2],
                      [0, _6EI_L2, _2EI_L, 0, -_6EI_L2, _4EI_L]])

        总体单刚 = self.坐标变换矩阵.transpose()@ 局部单刚@ self.坐标变换矩阵
        return 总体单刚

    def 计算结点固端力(self):
        '''[ FN , FS , M , FN , FS , M ]T'''
        self.局部固端力 = np.zeros(6)
        for _分布力 in self.分布力表:
            match (self.结点1.约束类型, self.结点2.约束类型):
                case ("固定支座" | "刚接", "铰支座" | "铰接"):
                    self.局部固端力[0] += 0
                    self.局部固端力[1] += (4*_分布力.Q1*self.l)/10+(9*_分布力.Q2*self.l)/40
                    self.局部固端力[2] += (_分布力.Q1*self.l**2)/15+(7*_分布力.Q2*self.l**2)/120
                    self.局部固端力[3] += 0
                    self.局部固端力[4] += (4*_分布力.Q1)/10 + (11*_分布力.Q2*self.l)/40
                    self.局部固端力[5] += 0
                case ("固定支座" | "刚接", "固定支座" | "刚接"):
                    self.局部固端力[0] += 0
                    self.局部固端力[1] += (7*_分布力.Q1*self.l)/20 + (3*_分布力.Q2*self.l)/20
                    self.局部固端力[2] += (_分布力.Q1*self.l**2)/20 + (_分布力.Q2*self.l**2)/30
                    self.局部固端力[3] += 0
                    self.局部固端力[4] += (3*_分布力.Q1*self.l)/20+(7*_分布力.Q2*self.l)/20
                    self.局部固端力[5] += -(_分布力.Q1*self.l**2)/30-(_分布力.Q2*self.l**2)/20
                case ("铰支座" | "铰接", "铰支座" | "铰接"):
                    self.局部固端力[0] += 0
                    self.局部固端力[1] += (_分布力.Q1*self.l)/3 + (_分布力.Q2*self.l)/6
                    self.局部固端力[2] += 0
                    self.局部固端力[3] += 0
                    self.局部固端力[4] += (_分布力.Q1*self.l)/6+(_分布力.Q2*self.l)/3
                    self.局部固端力[5] += 0
        self.局部固端力 = self.局部固端力.reshape(self.局部固端力.shape[0], 1)
        整体固端力 = self.坐标变换矩阵.transpose() @ self.局部固端力
        
        return 整体固端力
