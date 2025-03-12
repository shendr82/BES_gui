# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:43:00 2022

@author: ShendR

This is a Class that connects BES GUI functions with the graphical interface.
By running this program you will strat BES GUI and ready to use.

The purpose of BES GUI is to make it easier for the user to enter BES measurement
parameters on a graphical interface, which saves the specific values in a cnf
file. This file is then used to set up the APDCAM for the next measurement.

"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon

from gui_dark_design import Ui_MainWindow
from toggle_swich import Switch
import rad_mot_enc_fit
from motor_interpolation import calibration
import BES_devices_switch

# import mast_shot.shot_details as shot
# from mast_shot.da_proxy import return_shot_and_state

from files.read_cnf import ReadConfig
from files.write_cnf import WriteConfig

import os
import subprocess
import sys
from datetime import datetime



class BES_GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
            # Toggle switch button
        self.swich = Switch(thumb_radius=11, track_radius=8)        
        self.gridLayout_8.addWidget(self.swich, 6, 1, 1, 1)
        
        # self.turn_off_script = BES_devices_switch.turn_off()
        # self.turn_on_script = BES_devices_switch.turn_on()
        
            # Load previous parameters from last BES_settings.cnf and radius calculator function
        self.datapath = self.setup_datapath()
        self.directory = ''
        self.cnf_file = os.path.join(self.datapath, 'BES_settings.cnf')
        # self.cnf_file = 'BES_settings.cnf'
        self.cnf_default_file = os.path.join(os.getcwd(), 'files', 'BES_default_settings.cnf')
        self.cnf_test_file = os.path.join(os.getcwd(), 'files', 'BES_settings_test.cnf')
        self.besStr = self.load_cnf()     
        # self.radius_calc = rad_mot_enc_fit      # Curve fit by ShendR
        self.radius_calc = calibration
        
            # Indicator and Shot number from MAST
        # self.shot_nr = shot.get_shot_number()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_signal)
        self.timer.start(10000)  # 10 seconds interval
        
            # File menu button actions
        self.actionOpen_cnf_file.triggered.connect(lambda: self.open_cnf())
        self.actionOpen_cnf_file.setShortcut('Ctrl+O')
        self.actionSave_Datapath.triggered.connect(lambda: self.save_datapath())
        self.actionSave_Datapath.setShortcut('Ctrl+S')
        self.actionExit_GUI.triggered.connect(lambda: self.close())
        self.actionExit_GUI.setShortcut('Ctrl+Q')        
        
        self.actionReadMe.triggered.connect(lambda: self.open_readme())
        self.actionReadMe.setShortcut('Ctrl+H')        

            # Pushbutton actions
        self.save_button.clicked.connect(lambda: self.save_cnf())
        self.load_button.clicked.connect(lambda: self.load_cnf())
        self.load_default_button.clicked.connect(lambda: self.default_val())
        self.exit_button.clicked.connect(lambda: self.close())
        self.hardware_button.toggled.connect(self.handle_toggle)
        # self.hardware_button.toggled.connect(lambda: BES_devices_switch.turn_on())
        
        
            # Enter pressesd actions
        self.length_line.returnPressed.connect(lambda: self.save_cnf())
        self.freque_combo.currentIndexChanged.connect(lambda: self.save_cnf())
        self.bias_v_1_line.returnPressed.connect(lambda: self.save_cnf())
        self.bias_v_2_line.returnPressed.connect(lambda: self.save_cnf())
        self.temp_line.returnPressed.connect(lambda: self.save_cnf())
        self.trigger_line.returnPressed.connect(lambda: self.save_cnf())
        self.clock_combo.currentIndexChanged.connect(lambda: self.save_cnf())
        self.bes_radius_line.returnPressed.connect(lambda: self.save_cnf())
        self.filter_temp_line.returnPressed.connect(lambda: self.save_cnf())
        self.mast_trigger_line.returnPressed.connect(lambda: self.save_cnf())


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
        
        
    def setup_datapath(self):
        try:            
            self.logbook("Reading datapath: ")
            if sys.platform == 'win32':
                files = 'files'
                directory = os.getcwd()
                thisdir = os.path.join(directory, files)
            elif (sys.platform == "linux") or (sys.platform == "linux2"):
                thisdir = '/home/muadmin/BES_DATAC/BES/xbt_test/'
            self.logbook("Datapath: " + thisdir)
            print(f'Current set datapath: {thisdir}')
     
        except:
            self.logbook("<span style=\"color:#ff0000\" >"+'Could not read datapath'+"</span>")
        return thisdir
        

        # Getting entered values from GUI
    def get_values(self):
        try:
            duration = eval(self.length_line.text())
            freq = eval(self.freque_combo.currentText())
            bias_1 = eval(self.bias_v_1_line.text())
            bias_2 = eval(self.bias_v_2_line.text())
            temp = eval(self.temp_line.text())
            trig_delay = eval(self.trigger_line.text())
            clock = self.clock_combo.currentText()
            stream_if = self.stream_combo.currentText()
            
            radius = eval(self.bes_radius_line.text())
            filter_temp = eval(self.filter_temp_line.text())
            start = eval(self.mast_trigger_line.text())
            
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')
            
        if 0.1 <= duration <= 10:
            duration = duration
        else:
            raise Exception('Measurement duration value error! BES_settings.cnf file not saved')
            
        if 0.1 <= freq <= 4:
            freq = int(freq * 1000000)
        else:
            raise Exception('Frequency (sample rate) error! BES_settings.cnf file not saved')
        
        if 300 <= bias_1 <= 450:
            bias_1 = bias_1
        else:
            raise Exception('Bias 1 interval error! BES_settings.cnf file not saved')
            
        if 300 <= bias_2 <= 450:
            bias_2 = bias_2
        else:
            raise Exception('Bias 2 interval error! BES_settings.cnf file not saved')
        
        if 15 <= temp <= 30:
            temp = temp
        else:
            raise Exception('APD temperature interval error! BES_settings.cnf file not saved')
        
        if 0 <= trig_delay <= 1e7:
            trig_delay = trig_delay
        else:
            raise Exception('Trigger delay interval error! BES_settings.cnf file not saved')
            
        if clock == 'External':
            clock = 1
        elif clock == 'Internal':
            clock = 0
        else:
            raise Exception('Clock error! Clock value is not saved')
            
        if 20 <= filter_temp <= 85:
            filter_temp = filter_temp
        else:
            raise Exception('Filter temperature interval error! BES_settings.cnf file not saved')
            
        if 0.7 <= radius <= 1.6:
            radius = radius
        else:
            raise Exception('Radius interval error! BES_settings.cnf file not saved')
            
        if start >= 100:
            start = round(-start/1000, 3)
        else:
            raise Exception('Start interval error! BES_settings.cnf file not saved')
        
        if self.swich.isChecked() == True:
            filter_type = 'core'
        elif self.swich.isChecked() == False:
            filter_type = 'edge'
        else:
            raise Exception('Filter type error. Could not get filter type so it is not saved')
            
        print(f'Duration: {duration} \n',
              f'Frequecy: {freq} \n', 
              f'Bias 1: {bias_1} \n', 
              f'Bias 2: {bias_2} \n',
              f'Temperture: {temp} \n', 
              f'trig_delay: {trig_delay} \n',
              f'Clock: {clock} \n',
              f'Filter temperature: {filter_temp} \n',
              f'Radius: {radius} \n', 
              f'Start: {start} \n',
              f'Filter type: {filter_type} \n')
        
        return [duration, freq, bias_1, bias_2, temp, trig_delay, 
                clock, filter_temp, radius, start, filter_type, stream_if]
    
    
    
        # Saving parameter values in BES_settings.cnf file
    def save_cnf(self):
        try:
            values = self.get_values()

            now = datetime.now().isoformat(' ', 'seconds')
            radius = values[8]
            self.besStr.stepperParams[0].viewRadius = values[8]
            
                # Mirror setup
            # mirror_motor = self.radius_calc.mirror_fit(radius)[0]
            # mirror_encoder = self.radius_calc.mirror_fit(radius)[5]  # curve fit by ShendR
            mirror_motor = self.radius_calc(radius)[0]
            mirror_encoder = mirror_motor / (-28.6)
            self.besStr.stepperParams[0].motor.stepsSet = round(mirror_motor)
            self.besStr.stepperParams[0].motor.limitLow = -2000
            self.besStr.stepperParams[0].motor.limitHigh = 117000 
            self.besStr.stepperParams[0].encoder.stepsSet = round(mirror_encoder)
            
                # Camera setup
            # camera_motor = self.radius_calc.camera_fit(radius)[0]
            # camera_encoder = self.radius_calc.camera_fit(radius)[5]     # curve fit by ShendR
            camera_motor = self.radius_calc(radius)[1]
            camera_encoder = camera_motor / (-6.25)
            self.besStr.stepperParams[1].motor.stepsSet = round(camera_motor)
            self.besStr.stepperParams[1].motor.limitLow = -1900
            self.besStr.stepperParams[1].motor.limitHigh = 25000
            self.besStr.stepperParams[1].encoder.stepsSet = round(camera_encoder)
            
                # Lens setup
            # lens_motor = self.radius_calc.lens_fit(radius)[0]
            # lens_encoder = self.radius_calc.lens_fit(radius)[5]        # curve fit by ShendR
            lens_motor = self.radius_calc(radius)[2]
            lens_encoder = lens_motor / (-6.25)
            
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
                
            self.besStr.stepperParams[3].motor.stepsSet = round(lens_motor)
            self.besStr.stepperParams[3].motor.limitLow = -6900
            self.besStr.stepperParams[3].motor.limitHigh = 124000
            self.besStr.stepperParams[3].encoder.stepsSet = round(lens_encoder)
            
                # APD parameters
            self.besStr.apdParams.duration = values[0]
            self.besStr.apdParams.rate = values[1]
            self.besStr.apdParams.apd_bias1 = values[2]
            self.besStr.apdParams.apd_bias2 = values[3]
            self.besStr.apdParams.temperature = values[4]
            self.besStr.apdParams.trigDelay = values[5]
            self.besStr.apdParams.clkSrc = values[6]
            self.besStr.apdParams.stream_if = values[11]
            self.besStr.apdParams.start = values[9]
            
            self.besStr.filterParams.temperature = values[7]
            self.besStr.filterParams.type = values[10]


            # Default, non-GUI parameters. If these somehow need to be
            # changed on a shot by shot basis, then adding GUI-specific
            # entry fields will become necessary.
            self.besStr.apdParams.trigSrc = 1 # 1 == HW trigger
            self.besStr.filterParams.th_low = 0 # temp. lower limit (deg C)
            self.besStr.filterParams.th_high = 85 # temp. upper limit (deg C)

            
            if os.path.exists(self.cnf_file):
                print('Datapath + cnf_file: ' + self.cnf_file)
                WriteConfig(self.cnf_file).writeFile(self.besStr)
                self.logbook(f'Entered parameters are saved in cnf file  -----  @ {str(now)}')
            else:
                self.logbook('File does not exist in current directory, check Datapath!')
                
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')

   
        # Loading parameter values from BES_settings.cnf file
    def load_cnf(self):
        try:
            file = 'BES_settings.cnf'
            datapath = self.datapath
            path = os.path.join(datapath, file)
            if os.path.isfile(path) == False:
                file = 'BES_default_settings.cnf'
                self.logbook('Error message:', text_color="#ff0000")
                self.logbook('Original BES_settings.cnf file not found. Default parameters file is loaded.',
                             text_color=' #facb3f ')
            else:
                print('Previous parameters are loaded\n')
                self.logbook('Previous parameters are loaded')

            self.besStr = ReadConfig(self.cnf_file).readFile()
            
            self.length_line.setText(str(self.besStr.apdParams.duration))
            self.freque_combo.setCurrentText(str(self.besStr.apdParams.rate/1000000))
            self.bias_v_1_line.setText(str(self.besStr.apdParams.apd_bias1))
            self.bias_v_2_line.setText(str(self.besStr.apdParams.apd_bias2))
            self.temp_line.setText(str(self.besStr.apdParams.temperature))
            self.trigger_line.setText(str(self.besStr.apdParams.trigDelay))
            self.clock_combo.setCurrentIndex(self.besStr.apdParams.clkSrc)
            
            self.bes_radius_line.setText(str(self.besStr.stepperParams[0].viewRadius))
            self.filter_temp_line.setText(str(self.besStr.filterParams.temperature))
            self.mast_trigger_line.setText(str(self.besStr.apdParams.start*-1000))
            
            self.edge_core_switch(self.besStr.filterParams.type)
            
            return self.besStr            
            
        except Exception as e:
            self.logbook('Exeption error message:', text_color="#ff0000")
            self.logbook(f'--  {str(e)}  --', text_color=' #facb3f ')
            print('Could not load previous parameters, so default parameters are loaded')
            self.logbook('Could not load previous parameters, so default parameters are loaded')
            self.default_val()
                    
 
        # Loading default parameter values from txt file
    def default_val(self):
        self.besStr = ReadConfig(self.cnf_default_file).readFile()

        
        self.length_line.setText(str(self.besStr.apdParams.duration))
        self.freque_combo.setCurrentText(str(self.besStr.apdParams.rate/1000000))
        self.bias_v_1_line.setText(str(self.besStr.apdParams.apd_bias1))
        self.bias_v_2_line.setText(str(self.besStr.apdParams.apd_bias2))
        self.temp_line.setText(str(self.besStr.apdParams.temperature))
        self.trigger_line.setText(str(self.besStr.apdParams.trigDelay))
        self.clock_combo.setCurrentIndex(self.besStr.apdParams.clkSrc)
        
        self.bes_radius_line.setText(str(self.besStr.stepperParams[0].viewRadius))
        self.filter_temp_line.setText(str(self.besStr.filterParams.temperature))
        self.mast_trigger_line.setText(str(self.besStr.apdParams.start*-1000))
        
        self.edge_core_switch(self.besStr.filterParams.type)
        
        print('Default parameters are loaded\n')
        self.logbook('Default parameters are loaded')
        
        return self.besStr
        
        
        # Run open BES_settings.cnf file
    def open_cnf(self):
        file = os.path.join(self.datapath, 'BES_settings.cnf')
        # os.startfile(file)
        if sys.platform == 'win32':
            os.startfile(file)
        elif (sys.platform == "linux") or (sys.platform == "linux2"):
            # file = os.path.join(self.datapath, 'BES_settings.cnf')
            subprocess.call(['gedit', file])
        self.logbook(f'BES_settings.cnf file is opened: -- {file} --')
        
    def save_datapath(self):
        dialog = QtWidgets.QInputDialog()
        text, ok = dialog.getText(self, "Set data path", "Enter path:")
        
        try:            
            if text:
                self.datapath = text
                self.logbook("New Datapath is given: " + str(self.datapath))
                print(self.datapath)
                print(ok)
                self.cnf_file = os.path.join(self.datapath, 'BES_settings.cnf')
                self.cnf_default_file = os.path.join(self.datapath, 'BES_default_settings.cnf')
                self.cnf_test_file = os.path.join(self.datapath, 'BES_settings_test.cnf')
            else:
                self.logbook("<span style=\"color:#ff0000\" >"+'No new datapath is given'+"</span>")
                
        except:
            self.logbook.append("<span style=\"color:#ff0000\" >"+'No new datapath is given'+"</span>")
                
    
        # Run open Readme.txt file
    def open_readme(self):
        directory = os.getcwd()
        file = os.path.join(directory, 'readme.txt')
        if sys.platform == 'win32':
            os.startfile(file)
        elif sys.platform == "linux" or sys.platform == "linux2":
            file = os.path.join(self.datapath, file)
            subprocess.call(['gedit', file])
            
    def edge_core_switch(self, filter_type):
        filter_type = filter_type
        if filter_type == 'core\n':
            self.swich.setChecked(True)
            self.logbook('Plasma CORE is mesured with APDCam')
        else:
            # self.swich.isChecked(False)
            self.logbook('Plasma EDGE is mesured with APDCam')
            
    def shot_number(self, shot_nr):
        # shot_nr_new = shot.get_shot_number()
        if shot_nr != self.shot_nr:
            self.shot_nr = shot_nr
            self.lcdNumber.setProperty("intValue", self.shot_nr) 
            self.logbook(f'MAST shot number: --- {self.shot_nr} ---')
        
    def set_indicator(self):
        if self.shot_and_state > 5:
            self.indicator.setChecked(True)
            self.indicator.setText('Plasma')
            self.indicator.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(170, 67, 68);\n"
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
            self.save_button.setEnabled(False)
            self.save_button.setStyleSheet("QPushButton{\n"
                                            "background-color: rgb(100,100,100);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid white;\n"
                                            "pressed: rgb(255, 255, 255);\n"
                                            "}\n")
            self.load_button.setEnabled(False)
            self.load_button.setStyleSheet("QPushButton{\n"
                                            "background-color: rgb(100,100,100);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid white;\n"
                                            "pressed: rgb(255, 255, 255);\n"
                                            "}\n")
            self.load_default_button.setEnabled(False)
            self.load_default_button.setStyleSheet("QPushButton{\n"
                                            "background-color: rgb(100,100,100);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid white;\n"
                                            "pressed: rgb(255, 255, 255);\n"
                                            "}\n")
            
    def update_signal(self):
        try:
        # last_pulse,MASTU_state = return_shot_and_state()
        # self.shot_and_state = MASTU_state
        # # self.indicator.setText(last_pulse)
        # self.shot_number(last_pulse)
        # # self.shot_and_state = 6
        # self.set_indicator()
        # self.shot_number()
            year, month, day, hour, minute, second, temp = self.read_log_file('read_temperature.log')
            self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(year, month, day), QtCore.QTime(hour, minute, second)))
            self.lcdNumber_2.setProperty("intValue", temp)
        except:
            pass
    
    def handle_toggle(self, checked):
       """Handle button toggle state"""
       if checked:
           BES_devices_switch.turn_on()
           self.logbook('BES hardware is turned ON')
       else:
           BES_devices_switch.turn_off()
           self.logbook('BES hardware is turned OFF')
           
    def read_log_file(self,filename='read_temperature.log'):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue  # Skip invalid lines

                datetime_str, temp_str = parts
                date_parts = list(map(int, datetime_str.split("-")))

                if len(date_parts) != 6:
                    continue  # Skip invalid lines

                year, month, day, hour, minute, second = date_parts
                temp = int(temp_str)

                return year, month, day, hour, minute, second, temp
            
    def start(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

        

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
    # gui = GUI()
    # gui.start()
    # sys.exit(gui.exec_())

