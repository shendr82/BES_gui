# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bes_gui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 921)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 1231, 861))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(1000, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 3, 0, 1, 3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setMinimumSize(QtCore.QSize(200, 0))
        self.label_31.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_31.setObjectName("label_31")
        self.gridLayout_8.addWidget(self.label_31, 1, 3, 1, 1)
        self.bes_radius_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.bes_radius_line.setMinimumSize(QtCore.QSize(150, 0))
        self.bes_radius_line.setObjectName("bes_radius_line")
        self.gridLayout_8.addWidget(self.bes_radius_line, 1, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setMinimumSize(QtCore.QSize(50, 0))
        self.label_30.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_30.setObjectName("label_30")
        self.gridLayout_8.addWidget(self.label_30, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setMinimumSize(QtCore.QSize(200, 0))
        self.label_32.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_32.setObjectName("label_32")
        self.gridLayout_8.addWidget(self.label_32, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 3, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setMinimumSize(QtCore.QSize(200, 0))
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 0, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setMinimumSize(QtCore.QSize(50, 0))
        self.label_29.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_29.setObjectName("label_29")
        self.gridLayout_8.addWidget(self.label_29, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 0, 1, 1, 1)
        self.filter_temp_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.filter_temp_line.setObjectName("filter_temp_line")
        self.gridLayout_8.addWidget(self.filter_temp_line, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setMinimumSize(QtCore.QSize(70, 0))
        self.label_27.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(900, 330))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.trigger_line = QtWidgets.QLineEdit(self.groupBox)
        self.trigger_line.setObjectName("trigger_line")
        self.gridLayout_7.addWidget(self.trigger_line, 6, 1, 1, 1)
        self.clock_combo = QtWidgets.QComboBox(self.groupBox)
        self.clock_combo.setObjectName("clock_combo")
        self.clock_combo.addItem("")
        self.clock_combo.addItem("")
        self.gridLayout_7.addWidget(self.clock_combo, 9, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setMinimumSize(QtCore.QSize(200, 0))
        self.label_22.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 2, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setMinimumSize(QtCore.QSize(200, 0))
        self.label_24.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setMinimumSize(QtCore.QSize(200, 0))
        self.label_26.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 6, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setMinimumSize(QtCore.QSize(200, 0))
        self.label_21.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 1, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setMinimumSize(QtCore.QSize(200, 50))
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 4, 4, 1, 1)
        self.temp_line = QtWidgets.QLineEdit(self.groupBox)
        self.temp_line.setObjectName("temp_line")
        self.gridLayout_7.addWidget(self.temp_line, 5, 1, 1, 1)
        self.bias_v_1_line = QtWidgets.QLineEdit(self.groupBox)
        self.bias_v_1_line.setObjectName("bias_v_1_line")
        self.gridLayout_7.addWidget(self.bias_v_1_line, 3, 1, 1, 1)
        self.freq_line = QtWidgets.QLineEdit(self.groupBox)
        self.freq_line.setObjectName("freq_line")
        self.gridLayout_7.addWidget(self.freq_line, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setMinimumSize(QtCore.QSize(50, 0))
        self.label_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setMinimumSize(QtCore.QSize(50, 0))
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 6, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(150, 50))
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMinimumSize(QtCore.QSize(50, 0))
        self.label_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setMinimumSize(QtCore.QSize(200, 0))
        self.label_25.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 5, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(50, 0))
        self.label_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 1, 2, 1, 1)
        self.length_line = QtWidgets.QLineEdit(self.groupBox)
        self.length_line.setMinimumSize(QtCore.QSize(150, 0))
        self.length_line.setObjectName("length_line")
        self.gridLayout_7.addWidget(self.length_line, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 11, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMinimumSize(QtCore.QSize(50, 0))
        self.label_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setMinimumSize(QtCore.QSize(50, 0))
        self.label_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 9, 0, 1, 1)
        self.bias_v_2_line = QtWidgets.QLineEdit(self.groupBox)
        self.bias_v_2_line.setObjectName("bias_v_2_line")
        self.gridLayout_7.addWidget(self.bias_v_2_line, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setMinimumSize(QtCore.QSize(200, 0))
        self.label_23.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_23.setObjectName("label_23")
        self.gridLayout_7.addWidget(self.label_23, 3, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(70, 50))
        self.label_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 5, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem8, 8, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem9, 4, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem10, 4, 1, 1, 1)
        self.exit_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exit_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.gridLayout_5.addWidget(self.exit_button, 7, 0, 1, 3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem11, 6, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.gridLayout_5.addWidget(self.save_button, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem13, 2, 1, 1, 1)
        self.load_default_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_default_button.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load_default_button.setFont(font)
        self.load_default_button.setObjectName("load_default_button")
        self.gridLayout_5.addWidget(self.load_default_button, 5, 1, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load_button.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load_button.setFont(font)
        self.load_button.setObjectName("load_button")
        self.gridLayout_5.addWidget(self.load_button, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_XML_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_XML_file.setObjectName("actionOpen_XML_file")
        self.actionReadMe = QtWidgets.QAction(MainWindow)
        self.actionReadMe.setObjectName("actionReadMe")
        self.menuFile.addAction(self.actionOpen_XML_file)
        self.menuHelp.addAction(self.actionReadMe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">-----   Welcome to BES GUI   -----</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "BES parameters"))
        self.label_31.setText(_translate("MainWindow", "[0.7 - 1.6] s"))
        self.label_30.setText(_translate("MainWindow", "[°C]"))
        self.label_12.setText(_translate("MainWindow", "Parameters"))
        self.label_32.setText(_translate("MainWindow", "[20 - 60] °C"))
        self.label_10.setText(_translate("MainWindow", "BES viewing radius:"))
        self.label_28.setText(_translate("MainWindow", "Interval range"))
        self.label_29.setText(_translate("MainWindow", "[m]"))
        self.label_27.setText(_translate("MainWindow", "Unit"))
        self.label_11.setText(_translate("MainWindow", "Filter temperature:"))
        self.groupBox.setTitle(_translate("MainWindow", "APDCAM - 10G"))
        self.clock_combo.setItemText(0, _translate("MainWindow", "External"))
        self.clock_combo.setItemText(1, _translate("MainWindow", "Internal"))
        self.label_22.setText(_translate("MainWindow", "[0.1 - 4] MHz"))
        self.label_24.setText(_translate("MainWindow", "[350 - 450] V"))
        self.label_6.setText(_translate("MainWindow", "Temperature:"))
        self.label_2.setText(_translate("MainWindow", "Measurement length:"))
        self.label_26.setText(_translate("MainWindow", "[1 - 1e7] us"))
        self.label_21.setText(_translate("MainWindow", "[0.1 - 10] s"))
        self.label_20.setText(_translate("MainWindow", "Interval range"))
        self.label_4.setText(_translate("MainWindow", "APD Bias voltage 1:"))
        self.label_3.setText(_translate("MainWindow", "Sampling frequency:"))
        self.label_18.setText(_translate("MainWindow", "[°C]"))
        self.label_8.setText(_translate("MainWindow", "Trigger delay:"))
        self.label_19.setText(_translate("MainWindow", "[us]"))
        self.label_9.setText(_translate("MainWindow", "APDCAM parameters"))
        self.label_16.setText(_translate("MainWindow", "[V]"))
        self.label_25.setText(_translate("MainWindow", "[15 - 30] °C"))
        self.label_14.setText(_translate("MainWindow", "[s]"))
        self.label_5.setText(_translate("MainWindow", "APD Bias voltage 2:"))
        self.label_15.setText(_translate("MainWindow", "[MHz]"))
        self.label_17.setText(_translate("MainWindow", "[V]"))
        self.label_7.setText(_translate("MainWindow", "External clock:"))
        self.label_23.setText(_translate("MainWindow", "[350 - 450] V"))
        self.label_13.setText(_translate("MainWindow", "Unit"))
        self.label.setText(_translate("MainWindow", "BES GUI"))
        self.exit_button.setText(_translate("MainWindow", "Exit GUI"))
        self.save_button.setText(_translate("MainWindow", "Save values"))
        self.load_default_button.setText(_translate("MainWindow", "Load defult values"))
        self.load_button.setText(_translate("MainWindow", "Load values"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_XML_file.setText(_translate("MainWindow", "Open XML file"))
        self.actionReadMe.setText(_translate("MainWindow", "ReadMe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())