from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
    QWidget,
)
from forms.lxqjq import Ui_MainWindow
from about import AboutDialog
from result import ResultWidget
from structuralCalc import *
import logging, os


def getlogger(filename):
    logger = logging.getLogger()
    path = f"{os.getcwd()}\\log"
    if not os.path.exists(path):
        os.mkdir(path)
    file_handler = logging.FileHandler(f"{path}\\{filename}", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter(
            "[%(levelname)s] %(asctime)s File %(pathname)s Line %(lineno)d\n%(message)s"
        )
    )
    logger.addHandler(file_handler)
    return logger


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.结构计算 = 结构计算()
        self.result = ResultWidget(self)
        self.about = AboutDialog(self)
        self.logger = getlogger("log.txt")

    @Slot()
    def on_aboutBtn_clicked(self):
        self.about.show()
    
    @Slot()
    def on_calcBtn_clicked(self):
        try:
            self.结构计算.计算前检查()
            self.result.show()
            self.结构计算.计算结点位移()
            self.结构计算.计算各单元杆端力()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_saveBtn_clicked(self):
        save_file_path, file_type = QFileDialog.getSaveFileName(
            self, caption="保存文件", filter="JSON (*.json)"
        )
        if len(save_file_path) > 0:
            with open(save_file_path, "w", encoding="utf-8") as f:
                f.write(self.结构计算.导出JSON数据())

    @Slot()
    def on_openBtn_clicked(self):
        open_file_path, file_type = QFileDialog.getOpenFileName(
            self, caption="打开文件", filter="JSON (*.json)"
        )
        if len(open_file_path) > 0:
            with open(open_file_path, "r", encoding="utf-8") as f:
                try:
                    self.结构计算 = 结构计算.导入JSON(f.read())
                    self.刷新面板()
                except Exception as e:
                    self.logger.exception(str(e))

    def 重置选择(self):
        try:
            del self.选择材料编号
        except:
            pass
        try:
            del self.选择结点编号
        except:
            pass
        try:
            del self.选择单元编号
        except:
            pass
        try:
            del self.选择位移结点编号
        except:
            pass
        try:
            del self.选择分布力编号
        except:
            pass
        try:
            del self.选择集中力编号
        except:
            pass

    def 清空面板(self):
        # 清空所有表格
        self.materialTable.setRowCount(0)
        self.pointTable.setRowCount(0)
        self.unitsTable.setRowCount(0)
        self.displacementTable.setRowCount(0)
        self.bothLoadsTable.setRowCount(0)
        self.singleLoadsTable.setRowCount(0)
        # 材料组
        self.materialType.setCurrentIndex(0)
        self.mE.clear()
        self.mI.clear()
        self.mA.clear()
        # 结点组
        self.pointX.clear()
        self.pointY.clear()
        self.pointType.setCurrentIndex(0)
        # 单元组
        self.point1CBox.clear()
        self.point2CBox.clear()
        self.materialCBox.clear()
        # 位移组
        self.displacementSelectPoint.clear()
        self.UX.clear()
        self.UY.clear()
        self.phi.clear()
        # 分布荷载组
        self.bothLoadsSelectUnit.clear()
        self.bothLoadsType.setCurrentIndex(0)
        self.bothLoadsValue1.clear()
        self.bothLoadsValue2.clear()
        # 集中荷载组
        self.singleLoadSelectUnit.clear()
        self.singleLoadType.setCurrentIndex(0)
        self.singleLoadValue.clear()

    def 刷新面板(self):
        self.重置选择()
        self.清空面板()
        for 索引, _材料 in enumerate(self.结构计算.材料表):
            self.materialTable.insertRow(索引)
            self.materialTable.setItem(索引, 0, QTableWidgetItem(str(_材料.编号)))
            self.materialTable.setItem(索引, 1, QTableWidgetItem(str(_材料.类型)))
            self.materialTable.setItem(索引, 2, QTableWidgetItem(str(_材料.刚度)))
            self.materialTable.setItem(索引, 3, QTableWidgetItem(str(_材料.静矩)))
            self.materialTable.setItem(索引, 4, QTableWidgetItem(str(_材料.横截面积)))

            self.materialCBox.addItem(str(_材料.编号))

        for 索引, _结点 in enumerate(self.结构计算.结点表):
            self.pointTable.insertRow(索引)
            self.pointTable.setItem(索引, 0, QTableWidgetItem(str(_结点.编号)))
            self.pointTable.setItem(索引, 1, QTableWidgetItem(str(_结点.X坐标)))
            self.pointTable.setItem(索引, 2, QTableWidgetItem(str(_结点.Y坐标)))
            self.pointTable.setItem(索引, 3, QTableWidgetItem(str(_结点.约束类型)))

            self.point1CBox.addItem(str(_结点.编号))
            self.point2CBox.addItem(str(_结点.编号))

            self.singleLoadSelectUnit.addItem(str(_结点.编号))

        for 索引, _单元 in enumerate(self.结构计算.单元表):
            self.unitsTable.insertRow(索引)
            self.unitsTable.setItem(索引, 0, QTableWidgetItem(str(_单元.编号)))
            self.unitsTable.setItem(索引, 1, QTableWidgetItem(str(_单元.结点1)))
            self.unitsTable.setItem(索引, 2, QTableWidgetItem(str(_单元.结点2)))
            self.unitsTable.setItem(索引, 3, QTableWidgetItem(str(_单元.材料)))

            self.bothLoadsSelectUnit.addItem(str(_单元.编号))

        for 索引, _位移 in enumerate(self.结构计算.位移表):
            self.displacementTable.insertRow(索引)
            self.displacementTable.setItem(索引, 0, QTableWidgetItem(str(_位移.结点编号)))
            self.displacementTable.setItem(索引, 1, QTableWidgetItem(str(_位移.UX)))
            self.displacementTable.setItem(索引, 2, QTableWidgetItem(str(_位移.UY)))
            self.displacementTable.setItem(索引, 3, QTableWidgetItem(str(_位移.Φ)))

        for 索引, _分布力 in enumerate(self.结构计算.分布力表):
            self.bothLoadsTable.insertRow(索引)
            self.bothLoadsTable.setItem(索引, 0, QTableWidgetItem(str(_分布力.编号)))
            self.bothLoadsTable.setItem(索引, 1, QTableWidgetItem(str(_分布力.单元编号)))
            self.bothLoadsTable.setItem(索引, 2, QTableWidgetItem(str(_分布力.类型)))
            self.bothLoadsTable.setItem(索引, 3, QTableWidgetItem(str(_分布力.Q1)))
            self.bothLoadsTable.setItem(索引, 4, QTableWidgetItem(str(_分布力.Q2)))

        for 索引, _集中力 in enumerate(self.结构计算.集中力表):
            self.singleLoadsTable.insertRow(索引)
            self.singleLoadsTable.setItem(索引, 0, QTableWidgetItem(str(_集中力.编号)))
            self.singleLoadsTable.setItem(索引, 1, QTableWidgetItem(str(_集中力.结点编号)))
            self.singleLoadsTable.setItem(索引, 2, QTableWidgetItem(str(_集中力.类型)))
            self.singleLoadsTable.setItem(索引, 3, QTableWidgetItem(str(_集中力.F)))

    def 获取材料(self):
        材料类型 = self.materialType.currentText()
        刚度 = self.mE.text()
        静矩 = self.mI.text()
        横截面积 = self.mA.text()
        if len(材料类型) != 0 and len(刚度) != 0 and len(静矩) != 0 and len(横截面积) != 0:
            return 材料(材料类型, 刚度, 静矩, 横截面积)
        else:
            raise ValueError("请输入完整内容")

    def 获取结点(self):
        X坐标 = self.pointX.text()
        Y坐标 = self.pointY.text()
        约束类型 = self.pointType.currentText()
        if len(X坐标) != 0 and len(Y坐标) != 0 and len(约束类型) != 0:
            return 结点(X坐标, Y坐标, 约束类型)
        else:
            raise ValueError("请输入完整内容")

    def 获取单元(self):
        结点1 = self.point1CBox.currentText()
        结点2 = self.point2CBox.currentText()
        材料 = self.materialCBox.currentText()
        if len(结点1) != 0 and len(结点2) != 0 and len(材料) != 0:
            return 单元(
                self.结构计算.结点表[self.结构计算.结点表.index(int(结点1))],
                self.结构计算.结点表[self.结构计算.结点表.index(int(结点2))],
                self.结构计算.材料表[self.结构计算.材料表.index(int(材料))],
            )
        else:
            raise ValueError("请输入完整内容")

    def 获取位移(self):
        结点编号 = self.displacementSelectPoint.text()
        UX = self.UX.text()
        UY = self.UY.text()
        Φ = self.phi.text()
        if len(结点编号) != 0 and len(UX) != 0 and len(UY) != 0:
            return 位移(结点编号, UX, UY, Φ)
        else:
            raise ValueError("请输入完整内容")

    def 获取分布力(self):
        单元编号 = self.bothLoadsSelectUnit.currentText()
        类型 = self.bothLoadsType.currentText()
        Q1 = self.bothLoadsValue1.text()
        Q2 = self.bothLoadsValue2.text()
        if len(单元编号) != 0 and len(类型) != 0 and len(Q1) != 0 and len(Q2) != 0:
            return 分布力(单元编号, 类型, Q1, Q2)
        else:
            raise ValueError("请输入完整内容")

    def 获取集中力(self):
        结点编号 = self.singleLoadSelectUnit.currentText()
        类型 = self.singleLoadType.currentText()
        F = self.singleLoadValue.text()
        if len(结点编号) != 0 and len(类型) != 0 and len(F) != 0:
            return 集中力(结点编号, 类型, F)
        else:
            raise ValueError("请输入完整内容")

    @Slot(int, int)
    def on_materialTable_cellClicked(self, row, column):
        self.选择材料编号 = int(self.materialTable.item(row, 0).text())
        self.materialType.setCurrentIndex(
            材料类型表.index(self.materialTable.item(row, 1).text())
        )
        self.mE.setText(self.materialTable.item(row, 2).text())
        self.mI.setText(self.materialTable.item(row, 3).text())
        self.mA.setText(self.materialTable.item(row, 4).text())

    @Slot(int, int)
    def on_pointTable_cellClicked(self, row, column):
        self.选择结点编号 = int(self.pointTable.item(row, 0).text())
        self.pointX.setText(self.pointTable.item(row, 1).text())
        self.pointY.setText(self.pointTable.item(row, 2).text())
        self.pointType.setCurrentIndex(结点类型表.index(self.pointTable.item(row, 3).text()))

    @Slot(int, int)
    def on_unitsTable_cellClicked(self, row, column):
        结点编号表 = [str(x.编号) for x in self.结构计算.结点表]
        材料编号表 = [str(x.编号) for x in self.结构计算.材料表]

        self.选择单元编号 = int(self.unitsTable.item(row, 0).text())

        self.point1CBox.setCurrentIndex(
            结点编号表.index(self.unitsTable.item(row, 1).text())
        )
        self.point2CBox.setCurrentIndex(
            结点编号表.index(self.unitsTable.item(row, 2).text())
        )
        self.materialCBox.setCurrentIndex(
            材料编号表.index(self.unitsTable.item(row, 3).text())
        )

    @Slot(int, int)
    def on_displacementTable_cellClicked(self, row, column):
        self.选择位移结点编号 = int(self.displacementTable.item(row, 0).text())
        self.displacementSelectPoint.setText(self.displacementTable.item(row, 0).text())
        self.UX.setText(self.displacementTable.item(row, 1).text())
        self.UY.setText(self.displacementTable.item(row, 2).text())
        self.phi.setText(self.displacementTable.item(row, 3).text())

    @Slot(int, int)
    def on_bothLoadsTable_cellClicked(self, row, column):
        单元编号表 = [str(x.编号) for x in self.结构计算.单元表]

        self.选择分布力编号 = int(self.bothLoadsTable.item(row, 0).text())
        self.bothLoadsSelectUnit.setCurrentIndex(
            单元编号表.index(self.bothLoadsTable.item(row, 1).text())
        )
        self.bothLoadsType.setCurrentIndex(
            分布力类型表.index(self.bothLoadsTable.item(row, 2).text())
        )
        self.bothLoadsValue1.setText(self.bothLoadsTable.item(row, 3).text())
        self.bothLoadsValue2.setText(self.bothLoadsTable.item(row, 4).text())

    @Slot(int, int)
    def on_singleLoadsTable_cellClicked(self, row, column):
        结点编号表 = [str(x.编号) for x in self.结构计算.结点表]

        self.选择集中力编号 = int(self.singleLoadsTable.item(row, 0).text())
        self.singleLoadSelectUnit.setCurrentIndex(
            结点编号表.index(self.singleLoadsTable.item(row, 1).text())
        )
        self.singleLoadType.setCurrentIndex(
            集中力类型表.index(self.singleLoadsTable.item(row, 2).text())
        )
        self.singleLoadValue.setText(self.singleLoadsTable.item(row, 3).text())

    @Slot()
    def on_addMaterialBtn_clicked(self):
        try:
            新材料 = self.获取材料()
            self.结构计算.添加(新材料)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_addPointBtn_clicked(self):
        try:
            新结点 = self.获取结点()
            self.结构计算.添加(新结点)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_addUnitBtn_clicked(self):
        try:
            新单元 = self.获取单元()
            self.结构计算.添加(新单元)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_addBothLoadsBtn_clicked(self):
        try:
            新分布力 = self.获取分布力()
            self.结构计算.添加(新分布力)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_addSingleLoadBtn_clicked(self):
        try:
            新集中力 = self.获取集中力()
            self.结构计算.添加(新集中力)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_modifyMaterialBtn_clicked(self):
        try:
            self.选择材料编号
            新材料 = self.获取材料()
            self.结构计算.修改(新材料, self.选择材料编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_modifyPointBtn_clicked(self):
        try:
            self.选择结点编号
            新结点 = self.获取结点()
            self.结构计算.修改(新结点, self.选择结点编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_modifyUnitBtn_clicked(self):
        try:
            self.选择单元编号
            新单元 = self.获取单元()
            self.结构计算.修改(新单元, self.选择单元编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_acceptDisplacementBtn_clicked(self):
        try:
            self.选择位移结点编号
            新位移 = self.获取位移()
            self.结构计算.修改(新位移, self.选择位移结点编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_modifyBothLoadsBtn_clicked(self):
        try:
            self.选择分布力编号
            新分布力 = self.获取分布力()
            self.结构计算.修改(新分布力, self.选择分布力编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_modifySingleLoadBtn_clicked(self):
        try:
            self.选择集中力编号
            新集中力 = self.获取集中力()
            self.结构计算.修改(新集中力, self.选择集中力编号)
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_removeMaterialBtn_clicked(self):
        try:
            self.选择材料编号
            self.结构计算.删除(self.选择材料编号, "材料")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", "请选择材料")
            self.logger.exception(str(e))

    @Slot()
    def on_removePointBtn_clicked(self):
        try:
            self.选择结点编号
            self.结构计算.删除(self.选择结点编号, "结点")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", "请选择结点")
            self.logger.exception(str(e))

    @Slot()
    def on_removeUnitBtn_clicked(self):
        try:
            self.选择单元编号
            self.结构计算.删除(self.选择单元编号, "单元")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_clearDisplacementBtn_clicked(self):
        try:
            self.选择位移结点编号
            self.结构计算.删除(self.选择位移结点编号, "位移")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.error

    @Slot()
    def on_removeBothLoadsBtn_clicked(self):
        try:
            self.选择分布力编号
            self.结构计算.删除(self.选择分布力编号, "分布力")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))

    @Slot()
    def on_removeSingleLoadBtn_clicked(self):
        try:
            self.选择集中力编号
            self.结构计算.删除(self.选择集中力编号, "集中力")
            self.刷新面板()
        except Exception as e:
            QMessageBox.information(self, "提示", str(e))
            self.logger.exception(str(e))
