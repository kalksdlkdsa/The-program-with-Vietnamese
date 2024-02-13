
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ung_dung_ban_ve = QtWidgets.QLabel(parent=self.centralwidget)
        self.ung_dung_ban_ve.setGeometry(QtCore.QRect(260, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.ung_dung_ban_ve.setFont(font)
        self.ung_dung_ban_ve.setObjectName("ung_dung_ban_ve")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 80, 701, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 49, 16))
        self.label_2.setObjectName("label_2")
        self.ho_ten = QtWidgets.QLineEdit(parent=self.groupBox)
        self.ho_ten.setGeometry(QtCore.QRect(120, 50, 261, 21))
        self.ho_ten.setObjectName("ho_ten")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 51, 16))
        self.label_3.setObjectName("label_3")
        self.gioi_tinh = QtWidgets.QComboBox(parent=self.groupBox)
        self.gioi_tinh.setGeometry(QtCore.QRect(140, 110, 68, 22))
        self.gioi_tinh.setObjectName("gioi_tinh")
        self.gioi_tinh.addItem("")
        self.gioi_tinh.setItemText(0, "")
        self.gioi_tinh.addItem("")
        self.gioi_tinh.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 270, 701, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ca_phe = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.ca_phe.setGeometry(QtCore.QRect(40, 40, 75, 20))
        self.ca_phe.setObjectName("ca_phe")
        self.bim_bim = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.bim_bim.setGeometry(QtCore.QRect(440, 50, 75, 20))
        self.bim_bim.setObjectName("bim_bim")
        self.nguoi_lon = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.nguoi_lon.setGeometry(QtCore.QRect(320, 130, 42, 22))
        self.nguoi_lon.setObjectName("nguoi_lon")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(200, 130, 61, 16))
        self.label_4.setObjectName("label_4")
        self.tre_em = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.tre_em.setGeometry(QtCore.QRect(320, 190, 42, 22))
        self.tre_em.setObjectName("tre_em")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(200, 190, 49, 16))
        self.label_5.setObjectName("label_5")
        self.tinh_tien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tinh_tien.setGeometry(QtCore.QRect(140, 520, 75, 24))
        self.tinh_tien.setObjectName("tinh_tien")
        self.tien_tra = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tien_tra.setGeometry(QtCore.QRect(270, 520, 251, 21))
        self.tien_tra.setObjectName("tien_tra")
        self.dong = QtWidgets.QLabel(parent=self.centralwidget)
        self.dong.setGeometry(QtCore.QRect(530, 520, 49, 16))
        self.dong.setObjectName("dong")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tinh_tien.clicked.connect(self.tt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ung_dung_ban_ve.setText(_translate("MainWindow", "Ứng dụng bán vé"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_2.setText(_translate("MainWindow", "Họ tên"))
        self.label_3.setText(_translate("MainWindow", "Giới tính"))
        self.gioi_tinh.setItemText(1, _translate("MainWindow", "Nam"))
        self.gioi_tinh.setItemText(2, _translate("MainWindow", "Nữ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dịch vụ"))
        self.ca_phe.setText(_translate("MainWindow", "Cà phê"))
        self.bim_bim.setText(_translate("MainWindow", "Bim bim"))
        self.label_4.setText(_translate("MainWindow", "Người lớn"))
        self.label_5.setText(_translate("MainWindow", "Trẻ em"))
        self.tinh_tien.setText(_translate("MainWindow", "Tiền trả"))
        self.dong.setText(_translate("MainWindow", "vnđ"))
    def tt(self):
        price = {
            "ca_phe": 100000,
            "bim_bim": 50000,
            "nguoi_lon": 200000,
            "tre_em":50000
        }
        tien_ca_phe = 0
        if (self.ca_phe.checkState()!=0):
            tien_ca_phe = price["ca_phe"]
        tien_bim_bim = 0
        if (self.bim_bim.checkState()!=0):
            tien_bim_bim = price["bim_bim"]
        tien_nguoi_lon = self.nguoi_lon.text()
        tien_nguoi_lon = int(tien_nguoi_lon) * price["nguoi_lon"]
        tien_tre_em = self.tre_em.text()
        tien_tre_em = int(tien_tre_em) * price["tre_em"]
        sum = tien_ca_phe + tien_bim_bim + tien_nguoi_lon + tien_tre_em
        self.tien_tra.setText(str(sum)) # Đưa tiền vào khung tiền
        msg = QtWidgets.QMessageBox() # Khởi tạo cửa sổ thông báo (kiểu vậy)
        msg.setInformativeText(f"Tổng tiền phải trả là: {sum}vnđ")
        msg.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
