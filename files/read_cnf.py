# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:39:40 2023

@author: ShendR
"""

from files.cnf_structure import CnfStructure
from files.cnf_error_handle import PureConfigFileRead

# from cnf_structure import CnfStructure
# from cnf_error_handle import PureConfigFileRead

class ReadConfig:
    def __init__(self, file_name):
        self.fileName = file_name
        self.besStr = CnfStructure().BESStr()

    def readFile(self):
        error = 0

        cfRead = PureConfigFileRead(self.fileName)

        self.besStr.apdParams.rate = cfRead.readUIntValue(error, "APDCAM", "RATE")
        self.besStr.apdParams.duration = cfRead.readDoubleValue(error, "APDCAM", "DURATION")
        self.besStr.apdParams.start = cfRead.readDoubleValue(error, "APDCAM", "START")
        self.besStr.apdParams.apd_bias1 = cfRead.readUShortValue(error, "APDCAM", "APD_BIAS_1")
        self.besStr.apdParams.apd_bias2 = cfRead.readUShortValue(error, "APDCAM", "APD_BIAS_2")
        self.besStr.apdParams.temperature = cfRead.readUShortValue(error, "APDCAM", "TEMPERATURE")
        self.besStr.apdParams.trigDelay = cfRead.readDoubleValue(error, "APDCAM", "APD_TRIG_DELAY")
        self.besStr.apdParams.clkSrc = cfRead.readUCharValue(error, "APDCAM", "CLK_SRC")
        self.besStr.apdParams.stream_if = cfRead.readStringValue(error, "APDCAM", "STREAM_IF")
        
        self.besStr.filterParams.type = cfRead.readStringValue(error, "FILTER_HEATER", "FILTER_TYPE")
        self.besStr.filterParams.temperature = cfRead.readUShortValue(error, "FILTER_HEATER", "TEMPERATURE")

        self.besStr.stepperParams[0].viewRadius = cfRead.readDoubleValue(error, "STEPPER_MIRROR", "VIEW_RADIUS")
        self.besStr.stepperParams[0].mirrorAngle = cfRead.readDoubleValue(error, "STEPPER_MIRROR", "MIRROR_ANGLE")
        self.besStr.stepperParams[0].motor.stepsSet = cfRead.readUIntValue(error, "STEPPER_MIRROR","M_STEPS_SET")
        self.besStr.stepperParams[0].motor.stepsInit = cfRead.readUIntValue(error, "STEPPER_MIRROR","M_STEPS_INIT")
        self.besStr.stepperParams[0].motor.maxSpeed = cfRead.readUShortValue(error, "STEPPER_MIRROR","M_MAX_SPEED")
        self.besStr.stepperParams[0].motor.holdCurrent = cfRead.readUShortValue(error, "STEPPER_MIRROR","M_HOLD_CURRENT")
        self.besStr.stepperParams[0].motor.timeOut = cfRead.readUShortValue(error, "STEPPER_MIRROR","M_TIMEOUT")
        self.besStr.stepperParams[0].motor.limitLow = cfRead.readIntValue(error, "STEPPER_MIRROR","M_LIMIT_LOW")
        self.besStr.stepperParams[0].motor.limitHigh = cfRead.readIntValue(error, "STEPPER_MIRROR","M_LIMIT_HIGH")
        self.besStr.stepperParams[0].motor.stepsPerDegree = cfRead.readDoubleValue(error, "STEPPER_MIRROR","M_STEPS_PER_DEGREE")
        self.besStr.stepperParams[0].motor.stepsOffset = cfRead.readIntValue(error, "STEPPER_MIRROR","M_STEPS_OFFSET")
        self.besStr.stepperParams[0].encoder.tolerance = cfRead.readUShortValue(error, "STEPPER_MIRROR", "E_STEPS_TOLERANCE")
        self.besStr.stepperParams[0].encoder.stepsSet = cfRead.readIntValue(error, "STEPPER_MIRROR", "E_STEPS_SET")
        self.besStr.stepperParams[0].encoder.stepsInit = cfRead.readIntValue(error, "STEPPER_MIRROR", "E_STEPS_INIT")
        self.besStr.stepperParams[0].encoder.stepsRatio = cfRead.readDoubleValue(error, "STEPPER_MIRROR", "E_STEPS_RATIO")
        self.besStr.stepperParams[0].encoder.stepsOffset = cfRead.readIntValue(error, "STEPPER_MIRROR", "E_STEPS_OFFSET")
        
        self.besStr.stepperParams[1].motor.stepsSet = cfRead.readUIntValue(error, "STEPPER_CAMERA","M_STEPS_SET")
        self.besStr.stepperParams[1].motor.stepsInit = cfRead.readUIntValue(error, "STEPPER_CAMERA","M_STEPS_INIT")
        self.besStr.stepperParams[1].motor.maxSpeed = cfRead.readUShortValue(error, "STEPPER_CAMERA","M_MAX_SPEED")
        self.besStr.stepperParams[1].motor.holdCurrent = cfRead.readUShortValue(error, "STEPPER_CAMERA","M_HOLD_CURRENT")
        self.besStr.stepperParams[1].motor.timeOut = cfRead.readUShortValue(error, "STEPPER_CAMERA","M_TIMEOUT")
        self.besStr.stepperParams[1].motor.limitLow = cfRead.readIntValue(error, "STEPPER_CAMERA","M_LIMIT_LOW")
        self.besStr.stepperParams[1].motor.limitHigh = cfRead.readIntValue(error, "STEPPER_CAMERA","M_LIMIT_HIGH")
        self.besStr.stepperParams[1].motor.stepsPerDegree = cfRead.readDoubleValue(error, "STEPPER_CAMERA","M_STEPS_PER_DEGREE")
        self.besStr.stepperParams[1].motor.stepsOffset = cfRead.readIntValue(error, "STEPPER_CAMERA","M_STEPS_OFFSET")
        self.besStr.stepperParams[1].encoder.tolerance = cfRead.readUShortValue(error, "STEPPER_CAMERA", "E_STEPS_TOLERANCE")
        self.besStr.stepperParams[1].encoder.stepsSet = cfRead.readIntValue(error, "STEPPER_CAMERA", "E_STEPS_SET")
        self.besStr.stepperParams[1].encoder.stepsInit = cfRead.readIntValue(error, "STEPPER_CAMERA", "E_STEPS_INIT")
        self.besStr.stepperParams[1].encoder.stepsRatio = cfRead.readDoubleValue(error, "STEPPER_CAMERA", "E_STEPS_RATIO")
        self.besStr.stepperParams[1].encoder.stepsOffset = cfRead.readIntValue(error, "STEPPER_CAMERA", "E_STEPS_OFFSET")
        
        self.besStr.stepperParams[2].motor.stepsSet = cfRead.readUIntValue(error, "STEPPER_FILTER","M_STEPS_SET")
        self.besStr.stepperParams[2].motor.stepsInit = cfRead.readUIntValue(error, "STEPPER_FILTER","M_STEPS_INIT")
        self.besStr.stepperParams[2].motor.maxSpeed = cfRead.readUShortValue(error, "STEPPER_FILTER","M_MAX_SPEED")
        self.besStr.stepperParams[2].motor.holdCurrent = cfRead.readUShortValue(error, "STEPPER_FILTER","M_HOLD_CURRENT")
        self.besStr.stepperParams[2].motor.timeOut = cfRead.readUShortValue(error, "STEPPER_FILTER","M_TIMEOUT")
        self.besStr.stepperParams[2].motor.limitLow = cfRead.readIntValue(error, "STEPPER_FILTER","M_LIMIT_LOW")
        self.besStr.stepperParams[2].motor.limitHigh = cfRead.readIntValue(error, "STEPPER_FILTER","M_LIMIT_HIGH")
        self.besStr.stepperParams[2].motor.stepsPerDegree = cfRead.readDoubleValue(error, "STEPPER_FILTER","M_STEPS_PER_DEGREE")
        self.besStr.stepperParams[2].motor.stepsOffset = cfRead.readIntValue(error, "STEPPER_FILTER","M_STEPS_OFFSET")
        self.besStr.stepperParams[2].encoder.tolerance = cfRead.readUShortValue(error, "STEPPER_FILTER", "E_STEPS_TOLERANCE")
        self.besStr.stepperParams[2].encoder.stepsSet = cfRead.readIntValue(error, "STEPPER_FILTER", "E_STEPS_SET")
        self.besStr.stepperParams[2].encoder.stepsInit = cfRead.readIntValue(error, "STEPPER_FILTER", "E_STEPS_INIT")
        self.besStr.stepperParams[2].encoder.stepsRatio = cfRead.readDoubleValue(error, "STEPPER_FILTER", "E_STEPS_RATIO")
        self.besStr.stepperParams[2].encoder.stepsOffset = cfRead.readIntValue(error, "STEPPER_FILTER", "E_STEPS_OFFSET")
        
        self.besStr.stepperParams[3].motor.stepsSet = cfRead.readUIntValue(error, "STEPPER_LENS","M_STEPS_SET")
        self.besStr.stepperParams[3].motor.stepsInit = cfRead.readUIntValue(error, "STEPPER_LENS","M_STEPS_INIT")
        self.besStr.stepperParams[3].motor.maxSpeed = cfRead.readUShortValue(error, "STEPPER_LENS","M_MAX_SPEED")
        self.besStr.stepperParams[3].motor.holdCurrent = cfRead.readUShortValue(error, "STEPPER_LENS","M_HOLD_CURRENT")
        self.besStr.stepperParams[3].motor.timeOut = cfRead.readUShortValue(error, "STEPPER_LENS","M_TIMEOUT")
        self.besStr.stepperParams[3].motor.limitLow = cfRead.readIntValue(error, "STEPPER_LENS","M_LIMIT_LOW")
        self.besStr.stepperParams[3].motor.limitHigh = cfRead.readIntValue(error, "STEPPER_LENS","M_LIMIT_HIGH")
        self.besStr.stepperParams[3].motor.stepsPerDegree = cfRead.readDoubleValue(error, "STEPPER_LENS","M_STEPS_PER_DEGREE")
        self.besStr.stepperParams[3].motor.stepsOffset = cfRead.readIntValue(error, "STEPPER_LENS","M_STEPS_OFFSET")
        self.besStr.stepperParams[3].encoder.tolerance = cfRead.readUShortValue(error, "STEPPER_LENS", "E_STEPS_TOLERANCE")
        self.besStr.stepperParams[3].encoder.stepsSet = cfRead.readIntValue(error, "STEPPER_LENS", "E_STEPS_SET")
        self.besStr.stepperParams[3].encoder.stepsInit = cfRead.readIntValue(error, "STEPPER_LENS", "E_STEPS_INIT")
        self.besStr.stepperParams[3].encoder.stepsRatio = cfRead.readDoubleValue(error, "STEPPER_LENS", "E_STEPS_RATIO")
        self.besStr.stepperParams[3].encoder.stepsOffset = cfRead.readIntValue(error, "STEPPER_LENS", "E_STEPS_OFFSET")
        

        return self.besStr
