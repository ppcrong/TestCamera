# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ic_camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.group_button = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_button.sizePolicy().hasHeightForWidth())
        self.group_button.setSizePolicy(sizePolicy)
        self.group_button.setObjectName("group_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.group_button)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 151, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.btn_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.btn_container.setContentsMargins(0, 0, 0, 0)
        self.btn_container.setObjectName("btn_container")
        self.btn_cam_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cam_open.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ic_camera_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_cam_open.setIcon(icon1)
        self.btn_cam_open.setObjectName("btn_cam_open")
        self.btn_container.addWidget(self.btn_cam_open)
        self.btn_cam_close = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cam_close.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ic_camera_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_cam_close.setIcon(icon2)
        self.btn_cam_close.setObjectName("btn_cam_close")
        self.btn_container.addWidget(self.btn_cam_close)
        self.horizontalLayout_3.addWidget(self.group_button)
        self.group_camera = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_camera.sizePolicy().hasHeightForWidth())
        self.group_camera.setSizePolicy(sizePolicy)
        self.group_camera.setObjectName("group_camera")
        self.label_cam_preview = QtWidgets.QLabel(self.group_camera)
        self.label_cam_preview.setGeometry(QtCore.QRect(10, 10, 441, 331))
        self.label_cam_preview.setText("")
        self.label_cam_preview.setObjectName("label_cam_preview")
        self.horizontalLayout_3.addWidget(self.group_camera)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TestCamera"))
        self.group_button.setTitle(_translate("MainWindow", "Camera Control"))
        self.btn_cam_open.setText(_translate("MainWindow", "Open Camera"))
        self.btn_cam_close.setText(_translate("MainWindow", "Close Camera"))
        self.group_camera.setTitle(_translate("MainWindow", "Camera Preview"))
import res.image._image_rc
