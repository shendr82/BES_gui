# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bes_gui_black5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 849)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgb(42, 52, 62);\n"
"color: rgb(150, 150, 150);\n"
"border-color: rgb(0, 0, 0);\n"
"    alternate-background-color: rgb(0, 0, 0);\n"
"}\n"
"QMenuBar{\n"
"background-color:  rgb(42, 52, 62);\n"
"color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"\n"
"    background-color:rgb(42, 52, 62);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QMenuBar::item::selected{\n"
"\n"
"    background-color: rgb(58, 59, 61);\n"
"    color: rgb(250, 203, 63);\n"
"}\n"
"QMenu{\n"
"\n"
"    background-color: rgb(42, 52, 62);\n"
"    color: #fff;\n"
"}\n"
"QMenu::item::selected{\n"
"\n"
"    background-color: rgb(58, 59, 61);\n"
"    color: rgb(250, 203, 63);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{border: rgb(24, 34, 44);\n"
"margin-top: 1.6em;\n"
"background-color: rgb(24, 34, 44);}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 3px;\n"
"    padding: 3 0 3 0;\n"
"border-color: rgb(24, 34, 44);\n"
"color: rgb(250, 203, 63);\n"
"background-color: rgb(42, 52, 62);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setMinimumSize(QtCore.QSize(50, 0))
        self.label_29.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.gridLayout_8.addWidget(self.label_29, 3, 2, 1, 1)
        self.mast_trigger_line = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mast_trigger_line.setFont(font)
        self.mast_trigger_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.mast_trigger_line.setText("")
        self.mast_trigger_line.setObjectName("mast_trigger_line")
        self.gridLayout_8.addWidget(self.mast_trigger_line, 5, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setMinimumSize(QtCore.QSize(150, 0))
        self.label_31.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_31.setObjectName("label_31")
        self.gridLayout_8.addWidget(self.label_31, 3, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 6, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setMinimumSize(QtCore.QSize(50, 0))
        self.label_30.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.gridLayout_8.addWidget(self.label_30, 4, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_33.setObjectName("label_33")
        self.gridLayout_8.addWidget(self.label_33, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 5, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 3, 0, 1, 1)
        self.bes_radius_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.bes_radius_line.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bes_radius_line.setFont(font)
        self.bes_radius_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.bes_radius_line.setObjectName("bes_radius_line")
        self.gridLayout_8.addWidget(self.bes_radius_line, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 7, 1, 1, 1)
        self.filter_temp_line = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filter_temp_line.setFont(font)
        self.filter_temp_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.filter_temp_line.setObjectName("filter_temp_line")
        self.gridLayout_8.addWidget(self.filter_temp_line, 4, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setMinimumSize(QtCore.QSize(150, 0))
        self.label_28.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 1, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setMinimumSize(QtCore.QSize(100, 0))
        self.label_27.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 4, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setMinimumSize(QtCore.QSize(150, 0))
        self.label_32.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_32.setObjectName("label_32")
        self.gridLayout_8.addWidget(self.label_32, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 4, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setStyleSheet("color: rgb(250, 203, 63);\n"
"background-color: rgb(250, 203, 63);\n"
"border-color: rgb(250, 203, 63);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_8.addWidget(self.line_2, 2, 0, 1, 6)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 200))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{border: rgb(24, 34, 44);\n"
"margin-top: 1.6em;\n"
"background-color: rgb(24, 34, 44);}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 3px;\n"
"    padding: 3 0 3 0;\n"
"border-color: rgb(24, 34, 44);\n"
"color: rgb(250, 203, 63);\n"
"background-color: rgb(42, 52, 62);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.trigger_line = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.trigger_line.setFont(font)
        self.trigger_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.trigger_line.setObjectName("trigger_line")
        self.gridLayout_7.addWidget(self.trigger_line, 9, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setStyleSheet("color: rgb(250, 203, 63);\n"
"background-color: rgb(250, 203, 63);\n"
"border-color: rgb(250, 203, 63);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 2, 0, 1, 6)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMinimumSize(QtCore.QSize(50, 0))
        self.label_16.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 6, 2, 1, 1)
        self.freque_combo = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.freque_combo.setFont(font)
        self.freque_combo.setStyleSheet("QComboBox{\n"
"background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(62, 72, 82);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 250, 250);\n"
"    selection-background-color: rgb(88, 98, 100)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 203, 63);\n"
"}\n"
"QComboBox QAbstractItemView:hover {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 250, 250)\n"
"}\n"
"")
        self.freque_combo.setObjectName("freque_combo")
        self.freque_combo.addItem("")
        self.freque_combo.addItem("")
        self.freque_combo.addItem("")
        self.freque_combo.addItem("")
        self.gridLayout_7.addWidget(self.freque_combo, 4, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setMinimumSize(QtCore.QSize(150, 0))
        self.label_26.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 9, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setMinimumSize(QtCore.QSize(150, 50))
        self.label_20.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 1, 3, 1, 1)
        self.temp_line = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.temp_line.setFont(font)
        self.temp_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.temp_line.setObjectName("temp_line")
        self.gridLayout_7.addWidget(self.temp_line, 8, 1, 1, 1)
        self.length_line = QtWidgets.QLineEdit(self.groupBox)
        self.length_line.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.length_line.setFont(font)
        self.length_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.length_line.setObjectName("length_line")
        self.gridLayout_7.addWidget(self.length_line, 3, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_37.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 0, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_39.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_39.setScaledContents(False)
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_7.addWidget(self.label_39, 0, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setMinimumSize(QtCore.QSize(50, 0))
        self.label_17.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 7, 2, 1, 1)
        self.bias_v_2_line = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.bias_v_2_line.setFont(font)
        self.bias_v_2_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.bias_v_2_line.setObjectName("bias_v_2_line")
        self.gridLayout_7.addWidget(self.bias_v_2_line, 7, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setMinimumSize(QtCore.QSize(150, 0))
        self.label_23.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_7.addWidget(self.label_23, 6, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setMinimumSize(QtCore.QSize(150, 0))
        self.label_24.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setMinimumSize(QtCore.QSize(50, 0))
        self.label_18.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 8, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 7, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setMinimumSize(QtCore.QSize(150, 0))
        self.label_21.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 9, 0, 1, 1)
        self.bias_v_1_line = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.bias_v_1_line.setFont(font)
        self.bias_v_1_line.setStyleSheet("background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"")
        self.bias_v_1_line.setObjectName("bias_v_1_line")
        self.gridLayout_7.addWidget(self.bias_v_1_line, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        self.label_15.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 4, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setMinimumSize(QtCore.QSize(150, 0))
        self.label_25.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 8, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(100, 50))
        self.label_13.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 1, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setMinimumSize(QtCore.QSize(50, 0))
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 9, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 7, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 8, 0, 1, 1)
        self.clock_combo = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clock_combo.setFont(font)
        self.clock_combo.setStyleSheet("QComboBox{\n"
"background-color: rgb(52, 62, 72);\n"
"color: rgb(250, 203, 63);\n"
"border: None;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QComboBox:pressed{\n"
"    background-color: rgb(62, 72, 82);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 250, 250);\n"
"    selection-background-color: rgb(88, 98, 100)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 203, 63);\n"
"}\n"
"QComboBox QAbstractItemView:hover {\n"
"    background-color: rgb(52, 62, 72);\n"
"    color: rgb(250, 250, 250)\n"
"}\n"
"")
        self.clock_combo.setObjectName("clock_combo")
        self.clock_combo.addItem("")
        self.clock_combo.addItem("")
        self.gridLayout_7.addWidget(self.clock_combo, 12, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(50, 0))
        self.label_14.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setMinimumSize(QtCore.QSize(150, 0))
        self.label_22.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 4, 3, 1, 1)
        self.indicator = QtWidgets.QPushButton(self.groupBox)
        self.indicator.setMinimumSize(QtCore.QSize(70, 30))
        self.indicator.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.indicator.setFont(font)
        self.indicator.setStyleSheet("QPushButton{\n"
"background-color: rgb(34, 109, 88);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(170, 67, 68);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(170, 67, 68);\n"
"}")
        self.indicator.setCheckable(False)
        self.indicator.setChecked(True)
        self.indicator.setDefault(True)
        self.indicator.setFlat(False)
        self.indicator.setObjectName("indicator")
        self.gridLayout_7.addWidget(self.indicator, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 12, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem10, 0, 5, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"background-color: rgb(24, 34, 44);\n"
"color: rgb(210, 180, 80);\n"
"border: None;\n"
"}")
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 25477.0)
        self.lcdNumber.setProperty("intValue", 25477)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_7.addWidget(self.lcdNumber, 0, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 5)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setMinimumSize(QtCore.QSize(200, 0))
        self.label_34.setMaximumSize(QtCore.QSize(320, 50))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(":/logo/FPLab at EK.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(42, 52, 62);\n"
"selection-color: rgb(52, 63, 81);\n"
"color: rgb(250, 250, 250);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(500, 100))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(24, 34, 44);\n"
"border: None;\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 6)
        spacerItem11 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 3, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem12, 2, 1, 1, 1)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"pressed: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(108, 98, 63);\n"
"}\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.gridLayout_5.addWidget(self.exit_button, 7, 0, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem13, 4, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem14, 6, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(150, 40))
        self.save_button.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"pressed: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(108, 98, 63);\n"
"}\n"
"")
        self.save_button.setObjectName("save_button")
        self.gridLayout_5.addWidget(self.save_button, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 5, 0, 1, 1)
        self.load_default_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_default_button.sizePolicy().hasHeightForWidth())
        self.load_default_button.setSizePolicy(sizePolicy)
        self.load_default_button.setMinimumSize(QtCore.QSize(150, 40))
        self.load_default_button.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.load_default_button.setFont(font)
        self.load_default_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"pressed: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(108, 98, 63);\n"
"}\n"
"")
        self.load_default_button.setObjectName("load_default_button")
        self.gridLayout_5.addWidget(self.load_default_button, 5, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 4, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem17, 8, 1, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy)
        self.load_button.setMinimumSize(QtCore.QSize(150, 40))
        self.load_button.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.load_button.setFont(font)
        self.load_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 34, 44);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"pressed: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 82, 56);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(108, 98, 63);\n"
"}\n"
"")
        self.load_button.setObjectName("load_button")
        self.gridLayout_5.addWidget(self.load_button, 3, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem18, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 2, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1373, 22))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_cnf_file = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.actionOpen_cnf_file.setFont(font)
        self.actionOpen_cnf_file.setObjectName("actionOpen_cnf_file")
        self.actionSave_datapath = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.actionSave_datapath.setFont(font)
        self.actionSave_datapath.setObjectName("actionSave_datapath")
        self.actionReadMe = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.actionReadMe.setFont(font)
        self.actionReadMe.setObjectName("actionReadMe")
        self.actionExit_GUI = QtWidgets.QAction(MainWindow)
        self.actionExit_GUI.setObjectName("actionExit_GUI")
        self.menuFile.addAction(self.actionOpen_cnf_file)
        self.menuFile.addAction(self.actionSave_datapath)
        self.menuFile.addAction(self.actionExit_GUI)
        self.menuHelp.addAction(self.actionReadMe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.length_line, self.bias_v_1_line)
        MainWindow.setTabOrder(self.bias_v_1_line, self.bias_v_2_line)
        MainWindow.setTabOrder(self.bias_v_2_line, self.temp_line)
        MainWindow.setTabOrder(self.temp_line, self.trigger_line)
        MainWindow.setTabOrder(self.trigger_line, self.clock_combo)
        MainWindow.setTabOrder(self.clock_combo, self.bes_radius_line)
        MainWindow.setTabOrder(self.bes_radius_line, self.filter_temp_line)
        MainWindow.setTabOrder(self.filter_temp_line, self.mast_trigger_line)
        MainWindow.setTabOrder(self.mast_trigger_line, self.save_button)
        MainWindow.setTabOrder(self.save_button, self.load_button)
        MainWindow.setTabOrder(self.load_button, self.load_default_button)
        MainWindow.setTabOrder(self.load_default_button, self.exit_button)
        MainWindow.setTabOrder(self.exit_button, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BES @ MAST"))
        self.groupBox_2.setTitle(_translate("MainWindow", "BES parameters"))
        self.label_29.setText(_translate("MainWindow", "[m]"))
        self.label_31.setText(_translate("MainWindow", "[0.7 - 1.6] s"))
        self.label_36.setText(_translate("MainWindow", "Filter type:"))
        self.label_30.setText(_translate("MainWindow", "[°C]"))
        self.label_33.setText(_translate("MainWindow", "MAST Trigger:"))
        self.label_12.setText(_translate("MainWindow", "Parameters"))
        self.label_11.setText(_translate("MainWindow", "Filter temperature:"))
        self.label_35.setText(_translate("MainWindow", "[ms]"))
        self.label_10.setText(_translate("MainWindow", "BES viewing radius:"))
        self.label_28.setText(_translate("MainWindow", "Interval  range"))
        self.label_27.setText(_translate("MainWindow", "Unit"))
        self.label_32.setText(_translate("MainWindow", "[20 - 60] °C"))
        self.groupBox.setTitle(_translate("MainWindow", "APDCAM - 10G"))
        self.label_9.setText(_translate("MainWindow", "APDCAM - 10G parameters"))
        self.label_3.setText(_translate("MainWindow", "Sampling frequency:"))
        self.label_16.setText(_translate("MainWindow", "[V]"))
        self.freque_combo.setItemText(0, _translate("MainWindow", "4"))
        self.freque_combo.setItemText(1, _translate("MainWindow", "2"))
        self.freque_combo.setItemText(2, _translate("MainWindow", "1"))
        self.freque_combo.setItemText(3, _translate("MainWindow", "0.5"))
        self.label_26.setText(_translate("MainWindow", "[1 - 1e7] us"))
        self.label_20.setText(_translate("MainWindow", "Interval  range"))
        self.label_37.setText(_translate("MainWindow", "Measuring in:"))
        self.label_39.setText(_translate("MainWindow", "Experiment number:"))
        self.label_17.setText(_translate("MainWindow", "[V]"))
        self.label_23.setText(_translate("MainWindow", "[350 - 450] V"))
        self.label_24.setText(_translate("MainWindow", "[350 - 450] V"))
        self.label_2.setText(_translate("MainWindow", "Measurement length:"))
        self.label_4.setText(_translate("MainWindow", "APD Bias voltage 1:"))
        self.label_18.setText(_translate("MainWindow", "[°C]"))
        self.label_21.setText(_translate("MainWindow", "[0.1 - 10] s"))
        self.label_8.setText(_translate("MainWindow", "Trigger delay:"))
        self.label_15.setText(_translate("MainWindow", "[MHz]"))
        self.label_25.setText(_translate("MainWindow", "[15 - 30] °C"))
        self.label_13.setText(_translate("MainWindow", "Unit"))
        self.label_19.setText(_translate("MainWindow", "[us]"))
        self.label_6.setText(_translate("MainWindow", "APD Temperature:"))
        self.clock_combo.setItemText(0, _translate("MainWindow", "External"))
        self.clock_combo.setItemText(1, _translate("MainWindow", "Internal"))
        self.label_14.setText(_translate("MainWindow", "[s]"))
        self.label_5.setText(_translate("MainWindow", "APD Bias voltage 2:"))
        self.label_22.setText(_translate("MainWindow", "[0.1 - 4] MHz"))
        self.indicator.setText(_translate("MainWindow", "Setup"))
        self.label_7.setText(_translate("MainWindow", "External clock:"))
        self.label.setText(_translate("MainWindow", "Beam Emission Spectroscopy - GUI"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Gothic\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">-----   Welcome to BES GUI   -----</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.6pt;\"><br /></p></body></html>"))
        self.exit_button.setText(_translate("MainWindow", "Exit GUI"))
        self.save_button.setText(_translate("MainWindow", "Save values"))
        self.load_default_button.setText(_translate("MainWindow", "Load defult values"))
        self.load_button.setText(_translate("MainWindow", "Load values"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_cnf_file.setText(_translate("MainWindow", "Open cnf file"))
        self.actionSave_datapath.setText(_translate("MainWindow", "Save datapath"))
        self.actionReadMe.setText(_translate("MainWindow", "ReadMe"))
        self.actionExit_GUI.setText(_translate("MainWindow", "Exit GUI"))

import bes_logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

