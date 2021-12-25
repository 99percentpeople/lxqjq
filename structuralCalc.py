from utils import *
from dataType import *

import json


class 结构计算:
    def __init__(self):
        self.材料表 = []
        self.结点表 = []
        self.单元表 = []

    def __getattr__(self, name):
        match name:
            case "集中力表":
                集中力表 = []
                for each in self.结点表:
                    集中力表.extend(each.集中力表)
                return 集中力表
            case "分布力表":
                分布力表 = []
                for each in self.单元表:
                    分布力表.extend(each.分布力表)
                return 分布力表
            case "位移表":
                位移表 = []
                for each in self.结点表:
                    位移表.append(each.位移)
                return 位移表
            case _:
                raise AttributeError(f"{name} is not a valid attribute")

    def 添加(self, _项目, _编号=None) -> int:
        match _项目:
            case 材料():
                if _编号 == None:
                    编号列表 = list(map(lambda x: x.编号, self.材料表))
                    _项目.编号 = 获取编号(编号列表)
                else:
                    _项目.编号 = _编号
                self.材料表.append(_项目)

            case 结点():
                if _编号 == None:
                    编号列表 = list(map(lambda x: x.编号, self.结点表))
                    _项目.编号 = 获取编号(编号列表)
                else:
                    _项目.编号 = _编号
                _项目.位移 = 位移(_项目.编号, 0, 0, 0)
                self.结点表.append(_项目)

            case 单元():
                try:
                    self.单元表.index(_项目)
                except ValueError:
                    if _编号 == None:
                        编号列表 = list(map(lambda x: x.编号, self.单元表))
                        _项目.编号 = 获取编号(编号列表)
                    else:
                        _项目.编号 = _编号
                    self.单元表.append(_项目)
                else:
                    raise ValueError("单元已存在")

            case 分布力():
                try:
                    self.单元表[self.单元表.index(_项目.单元编号)].分布力表.index(_项目)
                except ValueError:
                    if _编号 == None:
                        编号列表 = list(map(lambda x: x.编号, self.分布力表))
                        _项目.编号 = 获取编号(编号列表)
                    else:
                        _项目.编号 = _编号
                    self.单元表[self.单元表.index(_项目.单元编号)].分布力表.append(_项目)
                else:
                    raise ValueError("该分布力已存在")

            case 集中力():
                try:
                    self.结点表[self.结点表.index(_项目.结点编号)].集中力表.index(_项目)
                except ValueError:
                    if _编号 == None:
                        编号列表 = list(map(lambda x: x.编号, self.集中力表))
                        _项目.编号 = 获取编号(编号列表)
                    else:
                        _项目.编号 = _编号
                    self.结点表[self.结点表.index(_项目.结点编号)].集中力表.append(_项目)
                else:
                    raise ValueError("该集中力已存在")

            case _:
                raise ValueError("未知类型")

    def 修改(self, _项目, _编号: int):
        match  _项目:
            case 材料():
                _项目.编号 = int(_编号)

                for _单元 in filter(lambda x: x.材料 == _项目, self.单元表):
                    _单元.材料 = _项目
                self.材料表[self.材料表.index(_编号)] = _项目

            case 结点():
                _项目.编号 = int(_编号)
                _项目.位移 = 位移(_项目.编号, 0, 0, 0)
                self.结点表[self.结点表.index(_编号)] = _项目
                try:
                    self.单元表[self.单元表.index(_项目)].修改结点(_项目)
                except ValueError:
                    pass

            case 单元():
                try:
                    _项目.编号 = int(_编号)
                    self.单元表[self.单元表.index(_项目)] = _项目
                except ValueError:
                    raise ValueError("单元不存在")

            case 位移():
                _项目.编号 = int(_编号)
                self.结点表[self.结点表.index(_编号)].位移 = _项目

            case 分布力():
                try:
                    _项目.编号 = int(_编号)
                    单元编号 = self.分布力表[self.分布力表.index(_编号)].单元编号
                    _单元 = self.单元表[self.单元表.index(单元编号)]
                    _单元.分布力表[_单元.分布力表.index(_编号)] = _项目
                except ValueError:
                    raise ValueError("分布力不存在")

            case 集中力():
                try:
                    _项目.编号 = int(_编号)
                    结点编号 = self.集中力表[self.集中力表.index(_编号)].结点编号
                    _结点 = self.结点表[self.结点表.index(结点编号)]
                    _结点.集中力表[_结点.集中力表.index(_编号)] = _项目
                except ValueError:
                    raise ValueError("集中力不存在")

            case _:
                raise ValueError("未知类型")

    def 删除(self, _编号: int, 类型: str) -> None:
        match 类型:
            case "材料":
                self.材料表.remove(_编号)
                for x in filter(lambda x: x.材料 == _编号, self.单元表):
                    self.删除(x.编号, "单元")

            case "结点":
                self.结点表.remove(_编号)
                for x in filter(lambda x: x.结点1 == _编号 or x.结点2 == _编号, self.单元表):
                    self.删除(x.编号, "单元")

            case "单元":
                self.单元表.remove(_编号)

            case "位移":
                self.结点表[self.结点表.index(_编号)].位移.清空()

            case "分布力":
                for _单元 in self.单元表:
                    try:
                        _单元.分布力表.remove(_编号)
                    except ValueError:
                        pass
                    else:
                        break

            case "集中力":
                for _结点 in self.结点表:
                    try:
                        _结点.集中力表.remove(_编号)
                    except ValueError:
                        pass
                    else:
                        break

            case _:
                raise ValueError("未知类型")

    def 计算前检查(self):
        # 确保已添加单元
        if len(self.单元表) == 0:
            raise ValueError("请添加计算单元")
        
        # 确保每一个结点都添加了单元
        for _结点 in self.结点表:
            try:
                self.单元表.index(_结点)
            except ValueError:
                raise ValueError("有未连接的结点")
            
        # 确保铰接点和刚结点都同时连接两个单元
        for _结点 in self.结点表:
            if _结点.约束类型 == "固定支座" or _结点.约束类型 == "铰支座":
                continue
            elif len(list(filter(lambda x: x.结点1 == _结点 or x.结点2 == _结点, self.单元表))) >= 2:
                continue
            else:
                raise ValueError("有铰接点或刚结点只连接了一个单元")
                
    def 计算综合结点荷载(self):
        综合结点荷载 = np.zeros((len(self.结点表)*3, 1))
        for i, _结点 in enumerate(self.结点表):
            i *= 3
            for _单元 in filter(lambda x: x.结点1 == _结点, self.单元表):
                j = self.结点表.index(_单元.结点2)*3
                整体结点荷载 = -_单元.整体固端力.copy()
                for _集中力 in _单元.结点1.集中力表:
                    match _集中力.类型:
                        case "整体X方向力":
                            整体结点荷载[0, 0] += _集中力.F
                        case "整体Y方向力":
                            整体结点荷载[1, 0] += _集中力.F
                        case "弯矩":
                            整体结点荷载[2, 0] += _集中力.F
                for _集中力 in _单元.结点2.集中力表:
                    match _集中力.类型:
                        case "整体X方向力":
                            整体结点荷载[3, 0] += _集中力.F
                        case "整体Y方向力":
                            整体结点荷载[4, 0] += _集中力.F
                        case "弯矩":
                            整体结点荷载[5, 0] += _集中力.F
                综合结点荷载[i:i+3, 0] += 整体结点荷载[0:3, 0]
                综合结点荷载[j:j+3, 0] += 整体结点荷载[3:6, 0]

        return 综合结点荷载

    @classmethod
    def 导入JSON(cls, json_data: str):
        结构计算 = cls()
        dict_data = json.loads(json_data)
        for dict_材料 in dict_data["材料表"]:
            _材料 = 材料(
                dict_材料["类型"],
                dict_材料["刚度"],
                dict_材料["静矩"],
                dict_材料["横截面积"],
            )
            结构计算.添加(_材料, dict_材料["编号"])
        for dict_结点 in dict_data["结点表"]:
            _结点 = 结点(
                dict_结点["X坐标"],
                dict_结点["Y坐标"],
                dict_结点["约束类型"],
            )
            结构计算.添加(_结点, dict_结点["编号"])

        for dict_单元 in dict_data["单元表"]:

            _单元 = 单元(
                结构计算.结点表[结构计算.结点表.index(int(dict_单元["结点1"]["编号"]))],
                结构计算.结点表[结构计算.结点表.index(int(dict_单元["结点2"]["编号"]))],
                结构计算.材料表[结构计算.材料表.index(int(dict_单元["材料"]["编号"]))],
            )
            结构计算.添加(_单元, dict_单元["编号"])

            _结点1_位移 = 位移(
                dict_单元["结点1"]["位移"]["结点编号"],
                dict_单元["结点1"]["位移"]["UX"],
                dict_单元["结点1"]["位移"]["UY"],
                dict_单元["结点1"]["位移"]["Φ"],
            )
            _结点2_位移 = 位移(
                dict_单元["结点2"]["位移"]["结点编号"],
                dict_单元["结点2"]["位移"]["UX"],
                dict_单元["结点2"]["位移"]["UY"],
                dict_单元["结点2"]["位移"]["Φ"],
            )
            结构计算.修改(_结点1_位移, dict_单元["结点1"]["编号"])
            结构计算.修改(_结点2_位移, dict_单元["结点2"]["编号"])

            for dict_集中力 in dict_单元["结点1"]["集中力表"]:
                _集中力 = 集中力(
                    dict_集中力["结点编号"],
                    dict_集中力["类型"],
                    dict_集中力["F"],
                )
                结构计算.添加(_集中力, dict_集中力["编号"])
            for dict_集中力 in dict_单元["结点2"]["集中力表"]:
                _集中力 = 集中力(
                    dict_集中力["结点编号"],
                    dict_集中力["类型"],
                    dict_集中力["F"],
                )
                结构计算.添加(_集中力, dict_集中力["编号"])
            for dict_分布力表 in dict_单元["分布力表"]:
                _分布力 = 分布力(
                    dict_分布力表["单元编号"],
                    dict_分布力表["类型"],
                    dict_分布力表["Q1"],
                    dict_分布力表["Q2"]
                )
                结构计算.添加(_分布力, dict_分布力表["编号"])
        return 结构计算

    def 导出JSON数据(self):
        json_data = json.dumps(
            {
                "材料表": [{
                    "编号": _材料.编号,
                    "类型": _材料.类型,
                    "刚度": _材料.刚度,
                    "静矩": _材料.静矩,
                    "横截面积": _材料.横截面积,
                } for _材料 in self.材料表],
                "结点表": [{
                    "编号": _结点.编号,
                    "X坐标": _结点.X坐标,
                    "Y坐标": _结点.Y坐标,
                    "约束类型": _结点.约束类型,
                    "位移": {
                        "结点编号": _结点.位移.结点编号,
                        "UX": _结点.位移.UX,
                        "UY": _结点.位移.UY,
                        "Φ": _结点.位移.Φ
                    },
                    "集中力表": [{
                        "编号": _集中力.编号,
                        "结点编号": _集中力.结点编号,
                        "类型":  _集中力.类型,
                        "F": _集中力.F
                    } for _集中力 in _结点.集中力表]
                } for _结点 in self.结点表],
                "单元表": [{
                    "编号": _单元.编号,
                    "材料": {
                        "编号": _单元.材料.编号,
                        "类型": _单元.材料.类型,
                        "刚度": _单元.材料.刚度,
                        "静矩": _单元.材料.静矩,
                        "横截面积": _单元.材料.横截面积,
                    },
                    "结点1": {
                        "编号": _单元.结点1.编号,
                        "X坐标": _单元.结点1.X坐标,
                        "Y坐标": _单元.结点1.Y坐标,
                        "约束类型": _单元.结点1.约束类型,
                        "位移": {
                            "结点编号": _单元.结点1.位移.结点编号,
                            "UX": _单元.结点1.位移.UX,
                            "UY": _单元.结点1.位移.UY,
                            "Φ": _单元.结点1.位移.Φ
                        },
                        "集中力表": [{
                            "编号": _集中力.编号,
                            "结点编号": _集中力.结点编号,
                            "类型":  _集中力.类型,
                            "F": _集中力.F
                        } for _集中力 in _单元.结点1.集中力表]
                    },
                    "结点2": {
                        "编号": _单元.结点2.编号,
                        "X坐标": _单元.结点2.X坐标,
                        "Y坐标": _单元.结点2.Y坐标,
                        "约束类型": _单元.结点2.约束类型,
                        "位移": {
                            "结点编号": _单元.结点2.位移.结点编号,
                            "UX": _单元.结点2.位移.UX,
                            "UY": _单元.结点2.位移.UY,
                            "Φ": _单元.结点2.位移.Φ
                        },
                        "集中力表": [{
                            "编号": _集中力.编号,
                            "结点编号": _集中力.结点编号,
                            "类型":  _集中力.类型,
                            "F": _集中力.F
                        } for _集中力 in _单元.结点2.集中力表]
                    },
                    "分布力表": [{
                        "编号": _分布力.编号,
                        "单元编号": _分布力.单元编号,
                        "类型": _分布力.类型,
                        "Q1": _分布力.Q1,
                        "Q2": _分布力.Q2,
                    } for _分布力 in _单元.分布力表],
                } for _单元 in self.单元表]},
            ensure_ascii=False)
        return json_data

    def 计算整体刚度矩阵(self):
        整体刚度矩阵 = np.zeros((len(self.结点表)*3, len(self.结点表)*3))
        for i, _结点 in enumerate(self.结点表):
            i *= 3
            for _单元 in filter(lambda x: x.结点1 == _结点, self.单元表):
                j = self.结点表.index(_单元.结点2)*3
                整体刚度矩阵[i:i+3, i:i+3] += _单元.总体单刚[0:3, 0:3]
                整体刚度矩阵[i:i+3, j:j+3] += _单元.总体单刚[0:3, 3:6]
                整体刚度矩阵[j:j+3, i:i+3] += _单元.总体单刚[3:6, 0:3]
                整体刚度矩阵[j:j+3, j:j+3] += _单元.总体单刚[3:6, 3:6]

        return 整体刚度矩阵

    def 计算结点位移(self):
        整体刚度矩阵 = self.计算整体刚度矩阵()
        综合结点荷载 = self.计算综合结点荷载()
        删除行列表 = []

        print(f"---综合结点荷载---\n{综合结点荷载}")
        print(f"---整体刚度矩阵---\n{整体刚度矩阵}")
        
        for i, _结点 in enumerate(self.结点表):
            i *= 3
            match _结点.约束类型:
                case "固定支座":
                    删除行列表.extend(range(i, i+3))
                case "铰支座":
                    删除行列表.extend(range(i, i+2))

                case _:
                    pass

        整体刚度矩阵 = np.delete(整体刚度矩阵, 删除行列表, 0)
        整体刚度矩阵 = np.delete(整体刚度矩阵, 删除行列表, 1)
        综合结点荷载 = np.delete(综合结点荷载, 删除行列表, 0)
        
        print(f"---引入支承条件，删除行列---\n{删除行列表}")
        print(f"---简化综合结点荷载---\n{综合结点荷载}")    
        print(f"---简化整体刚度矩阵---\n{整体刚度矩阵}")
        
        结点位移 = np.linalg.solve(整体刚度矩阵, 综合结点荷载)
        保留行列表 = list(set([x for x in range(len(self.结点表)*3)]
                         ).difference(set(删除行列表)))

        结点位移矩阵 = np.zeros((len(self.结点表)*3, 1))
        for i, j in enumerate(保留行列表):
            结点位移矩阵[j, 0] = 结点位移[i, 0]
        
        print(f"---结点位移---\n{结点位移矩阵}")
        
        for i, _结点 in enumerate(self.结点表):
            i *= 3
            for _单元 in filter(lambda x: x.结点1 == _结点, self.单元表):
                j = self.结点表.index(_单元.结点2)*3
                位移矩阵 = np.take(
                    结点位移矩阵, [[i], [i+1], [i+2], [j], [j+1], [j+2]]).copy()

                位移矩阵[0, 0] += _单元.结点1.位移.UX
                位移矩阵[1, 0] += _单元.结点1.位移.UY
                位移矩阵[2, 0] += _单元.结点1.位移.Φ

                位移矩阵[3, 0] += _单元.结点2.位移.UX
                位移矩阵[4, 0] += _单元.结点2.位移.UY
                位移矩阵[5, 0] += _单元.结点2.位移.Φ
                _单元.位移矩阵 = 位移矩阵

        return 结点位移矩阵

    def 计算各单元杆端力(self):
        # 杆端力 = np.zeros((len(self.结点表)*3, 1))
        # for i, _结点 in enumerate(self.结点表):
        #     i *= 3
        #     for _单元 in filter(lambda x: x.结点1 == _结点, self.单元表):
        #         j = self.结点表.index(_单元.结点2)*3
        #         单元杆端力 = _单元.局部固端力 + \
        #             np.dot(np.dot(_单元.坐标变换矩阵, _单元.总体单刚), _单元.位移矩阵)

        #         杆端力[i:i+3, 0] += 单元杆端力[0:3, 0]
        #         杆端力[j:j+3, 0] += 单元杆端力[3:6, 0]
        # print(f"{杆端力}\n--------------")
        for _单元 in self.单元表:
            单元杆端力 = _单元.局部固端力 + _单元.坐标变换矩阵 @ _单元.总体单刚 @ _单元.位移矩阵
            print(f"------单元 {_单元.编号}------")
            print(f"---坐标变换矩阵--- \n{_单元.坐标变换矩阵}")
            print(f"---局部固端力--- \n{_单元.局部固端力}")
            print(f"---总体单刚--- \n{_单元.总体单刚}")
            print(f"---位移矩阵--- \n{_单元.位移矩阵}")
            print(f"---单元杆端力--- \n{单元杆端力}")
