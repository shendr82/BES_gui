# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:43:00 2022

@author: ShendR

This is a Class that connects BES GUI functions with the graphical interface.
By running this program you will strat BES GUI and ready to use.

The purpose of BES GUI is to make it easier for the user to enter BES measurement
parameters on a graphical interface, which saves the specific values in an XML
file. This XML file is then used to set up the APDCAM for the next measurement.

"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QMessageBox, QSystemTrayIcon

from bes_gui1 import Ui_MainWindow

from pathlib import Path
import xml.etree.ElementTree as ET

# import numpy as np
import os
import traceback, sys
from datetime import datetime



class BES_GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
            # Load previous parameters from last XML
        self.load_xml()     
        
            # File menu button actions
        self.actionOpen_XML_file.triggered.connect(lambda: self.open_xml())
        self.actionReadMe.triggered.connect(lambda: self.open_readme())

            # Pushbutton actions
        self.save_button.clicked.connect(lambda: self.save_xml())
        self.load_button.clicked.connect(lambda: self.load_xml())
        self.load_default_button.clicked.connect(lambda: self.default_val())
        self.exit_button.clicked.connect(lambda: self.close())


        # Setting up Logbook function
    def logbook(self, text='', text_color='black', font="MS Shell Dlg 2", size = '9.6pt'): 
        set_text = "<span style=\" font-family:text_font; font-size:text_size; color : text_color \" >" + text + "</span>"
        write = set_text.replace('text_font', font)
        write = write.replace('text_color', text_color)
        write = write.replace('text_size', size)                
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.ensureCursorVisible()
        self.textBrowser.setAlignment(QtCore.Qt.AlignLeft)
        self.textBrowser.append(write)
        self.textBrowser.append('')


        # Getting entered values from GUI
    def get_values(self):
        length = self.length_line.text()
        freq = self.freq_line.text()
        bias_1 = self.bias_v_1_line.text()
        bias_2 = self.bias_v_2_line.text()
        temp = self.temp_line.text()
        trigger = self.trigger_line.text()
        
        radius = self.bes_radius_line.text()
        filter_temp = self.filter_temp_line.text()
        
        return [length, freq, bias_1, bias_2, temp, trigger, radius, filter_temp]
    
    
        # Saving parameter values in XML file
    def save_xml(self):
        try:
            values = self.get_values()
            now = datetime.now()
            tree = tree = ET.parse('new_values.xml')
            root = tree.getroot()
            
            serial = root[0].set('serial', values[0])
            maxspeed = root[1][0].set('maxSpeed', values[1])
            timeout = root[4][0].set('timeOut', values[2])
            
            file = ET.ElementTree(root)
            file.write('new_values.xml')
            
            print(f'serial: {values[0]}\nmaxspeed: {values[1]}\ntimeout: {values[2]} ')
            self.logbook(f'Entered parameters are saved in XML  -----  @ {str(now)}')
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color='#800080')

   
        # Loading parameter values from XML file
    def load_xml(self):
        try:
            tree = tree = ET.parse('new_values.xml')
            root = tree.getroot()
            
            serial = root[0].get('serial')
            maxspeed = root[1][0].get('maxSpeed')
            timeout = root[4][0].get('timeOut')
            
            temp = self.temp_line.setText(serial)
            trigger = self.trigger_line.setText(maxspeed)
            
            print('Previous parameters are loaded\n')
            self.logbook('Previous parameters are loaded')
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color='#800080')
            print('Could not load previous parameters, so default parameters are loaded')
            self.logbook('Could not load previous parameters, so default parameters are loaded')
            self.default_val()
                    
 
        # Loading default parameter values from txt file
    def default_val(self):
        file = 'apd_default.txt'
        lines = open(file, 'r').readlines()
        
        values = []
        for i in range(7):
            x=lines[i].split('\t')
            values.append(x[0])
        
        self.length_line.setText(values[0])
        self.freq_line.setText(values[1])
        self.bias_v_1_line.setText(values[2])
        self.bias_v_2_line.setText(values[3])
        self.temp_line.setText(values[4])
        self.trigger_line.setText(values[5])
        
        print('Default parameters are loaded\n')
        self.logbook('Default parameters are loaded')
        
        
        # Run open XML file (in internet explorer)
    def open_xml(self):
        file = 'new_values.xml'
        os.startfile(file)
        self.logbook(f'XML file is opened: -- {file} --')
    
       
        # Run open Readme.txt file
    def open_readme(self):
        file = 'readme.txt'
        os.startfile(file)
        
        


def GUI():
    app = QtWidgets.QApplication([])
    # app_icon = QtGui.QIcon()
    # app_icon.addPixmap(QtGui.QPixmap('pstc-256x256.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
    # app.setWindowIcon(app_icon)
#    app.setWindowTitle("SPI sensor data")
    # trayIcon = QSystemTrayIcon(QtGui.QIcon('pstc-256x256.png'), parent=app)
    widget = BES_GUI()
    # trayIcon.show()
    widget.show() 
    app.exec_()    
         
if __name__ == '__main__':
    GUI()
