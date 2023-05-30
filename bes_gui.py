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
from PyQt5.QtWidgets import QSystemTrayIcon

from gui_dark_design import Ui_MainWindow
import rad_mot_enc_fit

# from pathlib import Path
import xml.etree.ElementTree as ET

import os
import subprocess
import sys
from datetime import datetime



class BES_GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
            # Load previous parameters from last XML
        self.load_xml()     
        self.radius_calc = rad_mot_enc_fit
        
            # File menu button actions
        self.actionOpen_XML_file.triggered.connect(lambda: self.open_xml())
        self.actionOpen_XML_file.setShortcut('Ctrl+O')
        self.actionExit_GUI.triggered.connect(lambda: self.close())
        self.actionExit_GUI.setShortcut('Ctrl+Q')        
        
        self.actionReadMe.triggered.connect(lambda: self.open_readme())
        self.actionReadMe.setShortcut('Ctrl+H')        

            # Pushbutton actions
        self.save_button.clicked.connect(lambda: self.save_xml())
        self.load_button.clicked.connect(lambda: self.load_xml())
        self.load_default_button.clicked.connect(lambda: self.default_val())
        self.exit_button.clicked.connect(lambda: self.close())
        
        line_list = ['bes_radius_line', 
                     'bias_v_1_line', 
                     'bias_v_2_line', 
                     'filter_temp_line', 
                     'freq_line', 
                     'length_line', 
                     'line', 
                     'line_2', 
                     'mast_trigger_line', 
                     'temp_line', 
                     'trigger_line']
        
            # Enter pressesd actions
        self.length_line.returnPressed.connect(lambda: self.save_xml())
        self.freq_line.returnPressed.connect(lambda: self.save_xml())
        self.bias_v_1_line.returnPressed.connect(lambda: self.save_xml())
        self.bias_v_2_line.returnPressed.connect(lambda: self.save_xml())
        self.temp_line.returnPressed.connect(lambda: self.save_xml())
        self.trigger_line.returnPressed.connect(lambda: self.save_xml())
        self.bes_radius_line.returnPressed.connect(lambda: self.save_xml())
        self.filter_temp_line.returnPressed.connect(lambda: self.save_xml())
        self.mast_trigger_line.returnPressed.connect(lambda: self.save_xml())


        # Setting up Logbook function
    def logbook(self, text='', text_color='white', font="Century Gothic", size = '9.6pt'): 
        set_text = "<span style=\" font-family:text_font; font-size:text_size; color : text_color \" >" + text + "</span>"
        write = set_text.replace('text_font', font)
        write = write.replace('text_color', text_color)
        write = write.replace('text_size', size)                
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.ensureCursorVisible()
        self.textBrowser.setAlignment(QtCore.Qt.AlignLeft)
        self.textBrowser.append(write)


        # Getting entered values from GUI
    def get_values(self):
        try:
            length = eval(self.length_line.text())
            freq = eval(self.freq_line.text())
            bias_1 = eval(self.bias_v_1_line.text())
            bias_2 = eval(self.bias_v_2_line.text())
            temp = eval(self.temp_line.text())
            trigger = eval(self.trigger_line.text())
            clock = self.clock_combo.currentText()
            
            radius = eval(self.bes_radius_line.text())
            filter_temp = eval(self.filter_temp_line.text())
            start = eval(self.mast_trigger_line.text())
            
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')
            
        if 0.1 <= length <= 10:
            length = length
        else:
            raise Exception('Interval error! XML file not saved')
            
        if 0.1 <= freq <= 4:
            freq = round(1/freq, 3)*1e-6
        else:
            raise Exception('Interval error! XML file not saved')
        
        if 350 <= bias_1 <= 450:
            bias_1 = bias_1
        else:
            raise Exception('Interval error! XML file not saved')
            
        if 350 <= bias_2 <= 450:
            bias_2 = bias_2
        else:
            raise Exception('Interval error! XML file not saved')
        
        if 15 <= temp <= 30:
            temp = temp
        else:
            raise Exception('Interval error! XML file not saved')
        
        if 0 <= trigger <= 1e7:
            trigger = trigger
        else:
            raise Exception('Interval error! XML file not saved')
            
        if 20 <= filter_temp <= 60:
            filter_temp = filter_temp
        else:
            raise Exception('Interval error! XML file not saved')
            
        if 0.7 <= radius <= 1.6:
            radius = radius
        else:
            raise Exception('Interval error! XML file not saved')
            
        if start >= 100:
            start = round(-start/1000, 3)
        else:
            raise Exception('Interval error! XML file not saved')
        
        return [length, freq, bias_1, bias_2, temp, trigger, clock, filter_temp, radius, start]
    
    
    
        # Saving parameter values in XML file
    def save_xml(self):
        try:
            values = self.get_values()
            # print(f'Values: {values}')
            now = datetime.now().isoformat(' ', 'seconds')
            radius = values[8]
            
            tree = tree = ET.parse('apd_parameters.xml')
            root = tree.getroot()

            lens_motor = self.radius_calc.lens_fit(radius)[0]
            lens_encoder = self.radius_calc.lens_fit(radius)[5]        
            
            if lens_motor > 123000:
                lens_motor = 123000
            else:
                lens_motor = lens_motor
            if radius == 1.6:
                lens_motor = 0
                
            if lens_encoder < -19680:
                lens_encoder = -19680
            else:
                lens_encoder = lens_encoder
            if radius == 1.6:
                lens_encoder = 0 
            
            mirror_param = self.radius_calc.mirror_fit(radius)
            camera_param = self.radius_calc.camera_fit(radius)
            
            root[0].set('duration', str(values[0]))                 # lenght
            root[0].set('interval', str(values[1]))                 # freq
            root[0].set('apd_bias_1', str(values[2]))               # bias_1
            root[0].set('apd_bias_2', str(values[3]))               # bias_2
            root[0].set('temperature', str(values[4]))              # temp
            root[0].set('apd_trig_delay', str(values[5]))           # trigger
            root[0].set('clock', values[6])                         # clock
            root[0].set('start', str(values[9]))                    # MAST trigger
            
            root[1].set('viewRadius', str(values[8]))               # radius
            root[5].set('temperature', str(values[7]))              # filter_temp
            
            root[1][0].set('stepsSet', str(round(mirror_param[0])))      # mirror motor
            root[1][1].set('stepsSet', str(round(mirror_param[5])))      # mirror encoder
            
            root[2][0].set('stepsSet', str(round(camera_param[0])))      # camera motor
            root[2][1].set('stepsSet', str(round(camera_param[5])))      # camera encoder
            
            root[4][0].set('stepsSet', str(round(lens_motor)))           # mirror motor
            root[4][1].set('stepsSet', str(round(lens_encoder)))         # mirror encoder
            
            file = ET.ElementTree(root)
            file.write('apd_parameters.xml')
            
            self.logbook(f'Entered parameters are saved in XML  -----  @ {str(now)}')
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')

   
        # Loading parameter values from XML file
    def load_xml(self):
        try:
            file = 'apd_parameters.xml'
            if os.path.isfile(file) == False:
                file = 'apd_parameters_default.xml'
                self.logbook('Error message:', text_color="#ff0000")
                self.logbook('Original apd_parameters.xml file not found. Default parameters file is loaded.',
                             text_color=' #facb3f ')
            else:
                print('Previous parameters are loaded\n')
                self.logbook('Previous parameters are loaded')
            tree = tree = ET.parse(file)
            root = tree.getroot()
            
            length = root[0].get('duration')
            freq = root[0].get('interval')
            freq1 = str(round(1e-6/eval(freq),1))
            bias_1 = root[0].get('apd_bias_1')
            bias_2 = root[0].get('apd_bias_2')
            temp = root[0].get('temperature')
            trigger = root[0].get('apd_trig_delay')
            clock = root[0].get('clock')
            
            radius = root[1].get('viewRadius')
            filter_temp= root[5].get('temperature')
            start = root[0].get('start')
            start1 = str(round(eval(start)*-1000))
            
            self.length_line.setText(length)
            self.freq_line.setText(freq1)
            self.bias_v_1_line.setText(bias_1)
            self.bias_v_2_line.setText(bias_2)
            self.temp_line.setText(temp)
            self.trigger_line.setText(trigger)
            self.clock_combo.setCurrentText(clock)
            
            self.bes_radius_line.setText(radius)
            self.filter_temp_line.setText(filter_temp)
            self.mast_trigger_line.setText(start1)
            
            
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')
            print('Could not load previous parameters, so default parameters are loaded')
            self.logbook('Could not load previous parameters, so default parameters are loaded')
            self.default_val()
                    
 
        # Loading default parameter values from txt file
    def default_val(self):
        file = 'apd_default.txt'
        lines = open(file, 'r').readlines()
        
        values = []
        for i in range(10):
            x=lines[i].split('\t')
            values.append(x[0])
        
        self.length_line.setText(values[0])
        self.freq_line.setText(values[1])
        self.bias_v_1_line.setText(values[2])
        self.bias_v_2_line.setText(values[3])
        self.temp_line.setText(values[4])
        self.trigger_line.setText(values[5])
        self.clock_combo.setCurrentIndex(0)
        
        self.bes_radius_line.setText(values[6])
        self.filter_temp_line.setText(values[7])
        self.mast_trigger_line.setText(str(round(eval(values[8])*-1000)))
        
        print('Default parameters are loaded\n')
        self.logbook('Default parameters are loaded')
        
        
        # Run open XML file (in internet explorer)
    def open_xml(self):
        file = 'apd_parameters.xml'
        # os.startfile(file)
        if sys.platform == 'win32':
            os.startfile(file)
        elif sys.platform == "linux" or sys.platform == "linux2":
            subprocess.call(['xdg-open', file])
        self.logbook(f'XML file is opened: -- {file} --')
    
       
        # Run open Readme.txt file
    def open_readme(self):
        file = 'readme.txt'
        # os.startfile(file)
        if sys.platform == 'win32':
            os.startfile(file)
        elif sys.platform == "linux" or sys.platform == "linux2":
            subprocess.call(['xdg-open', file])
        

def GUI():
    app = QtWidgets.QApplication([])
    app_icon = QtGui.QIcon()
    app_icon.addPixmap(QtGui.QPixmap('BES-MAST-256.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
    app.setWindowIcon(app_icon)
    trayIcon = QSystemTrayIcon(QtGui.QIcon('BES-MAST-256.png'), parent=app)
    widget = BES_GUI()
    trayIcon.show()
    widget.showMaximized()
    app.exec_()    
         
if __name__ == '__main__':
    GUI()
