# Form implementation generated from reading ui file 'D:\Study\Year2\TDLT\C7\DOANCUOIKI\MainWindow4.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 634)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 911, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Study\\Year2\\TDLT\\C7\\DOANCUOIKI\\../../../../../LINH TINH/UGOT-AI-City-Guardian-1.webp"))
        self.label.setObjectName("label")
        self.tableWidget1 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget1.setGeometry(QtCore.QRect(10, 30, 381, 241))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 370, 631, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 30, 251, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 70, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 120, 111, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 170, 111, 41))
        self.label_5.setObjectName("label_5")
        self.lineEditID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditID.setGeometry(QtCore.QRect(570, 70, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditID.setFont(font)
        self.lineEditID.setObjectName("lineEditID")
        self.lineEditTen = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTen.setGeometry(QtCore.QRect(570, 120, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTen.setFont(font)
        self.lineEditTen.setObjectName("lineEditTen")
        self.lineEditSL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSL.setGeometry(QtCore.QRect(570, 180, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSL.setFont(font)
        self.lineEditSL.setObjectName("lineEditSL")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEditTong = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTong.setGeometry(QtCore.QRect(280, 300, 301, 41))
        self.lineEditTong.setObjectName("lineEditTong")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(114, 310, 121, 20))
        self.label_6.setObjectName("label_6")
        self.pushDat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushDat.setGeometry(QtCore.QRect(710, 450, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushDat.setFont(font)
        self.pushDat.setObjectName("pushDat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên món"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Giá "))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tên món"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Số lượng"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Đơn giá"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">THÊM MÓN ĂN</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID Món ăn</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tên món</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Số lượng</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "THÊM "))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">TỔNG TIỀN</span></p></body></html>"))
        self.pushDat.setText(_translate("MainWindow", "ĐẶT HÀNG"))
