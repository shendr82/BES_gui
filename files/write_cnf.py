# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:34:49 2023

@author: ShendR
"""

# from files.cnf_structure import CnfStructure
# from cnf_structure import CnfStructure

class WriteConfig:
    def __init__(self, cFileName):
        self.fileName = cFileName
        # self.besStr = CnfStructure().BESStr()

    def writeFile(self, besStr):
        error = 0

        try:
            with open(self.fileName, 'w') as Setup:
                Setup.write("CONFIG FILE FOR MAST-U BES system\n")
                Setup.write("-------------------------------------\n\n")
                Setup.write("APDCAM\n\n")
                Setup.write("RATE {}\n".format(besStr.apdParams.rate))
                Setup.write("DURATION {}\n".format(besStr.apdParams.duration))
                Setup.write("START {}\n".format(besStr.apdParams.start))
                Setup.write("APD_BIAS_1 {}\n".format(besStr.apdParams.apd_bias1))
                Setup.write("APD_BIAS_2 {}\n".format(besStr.apdParams.apd_bias2))
                Setup.write("TEMPERATURE {}\n".format(besStr.apdParams.temperature))
                Setup.write("APD_TRIG_DELAY {}\n".format(besStr.apdParams.trigDelay))
                Setup.write("APD_TRIG_SRC {}\n".format(besStr.apdParams.trigSrc))
                Setup.write("CLK_SRC {}\n".format(besStr.apdParams.clkSrc))
                Setup.write("STREAM_IF {}\n\n".format(besStr.apdParams.stream_if))

                Setup.write("STEPPER_MIRROR\n\n")
                Setup.write("VIEW_RADIUS {}\n".format(besStr.stepperParams[0].viewRadius))
                Setup.write("MIRROR_ANGLE {}\n\n".format(besStr.stepperParams[0].mirrorAngle))

                Setup.write("M_STEPS_SET {}\n".format(besStr.stepperParams[0].motor.stepsSet))
                Setup.write("M_STEPS_INIT {}\n".format(besStr.stepperParams[0].motor.stepsInit))
                Setup.write("M_MAX_SPEED {}\n".format(besStr.stepperParams[0].motor.maxSpeed))
                Setup.write("M_HOLD_CURRENT {}\n".format(besStr.stepperParams[0].motor.holdCurrent))
                Setup.write("M_TIMEOUT {}\n".format(besStr.stepperParams[0].motor.timeOut))
                Setup.write("M_LIMIT_LOW {}\n".format(besStr.stepperParams[0].motor.limitLow))
                Setup.write("M_LIMIT_HIGH {}\n".format(besStr.stepperParams[0].motor.limitHigh))
                Setup.write("M_STEPS_PER_DEGREE {}\n".format(besStr.stepperParams[0].motor.stepsPerDegree))
                Setup.write("M_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[0].motor.stepsOffset))

                Setup.write("E_STEPS_TOLERANCE {}\n".format(besStr.stepperParams[0].encoder.tolerance))
                Setup.write("E_STEPS_SET {}\n".format(besStr.stepperParams[0].encoder.stepsSet))
                Setup.write("E_STEPS_INIT {}\n".format(besStr.stepperParams[0].encoder.stepsInit))
                Setup.write("E_STEPS_RATIO {}\n".format(besStr.stepperParams[0].encoder.stepsRatio))
                Setup.write("E_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[0].encoder.stepsOffset))

                Setup.write("STEPPER_CAMERA\n\n")
                Setup.write("M_STEPS_SET {}\n".format(besStr.stepperParams[1].motor.stepsSet))
                Setup.write("M_STEPS_INIT {}\n".format(besStr.stepperParams[1].motor.stepsInit))
                Setup.write("M_MAX_SPEED {}\n".format(besStr.stepperParams[1].motor.maxSpeed))
                Setup.write("M_HOLD_CURRENT {}\n".format(besStr.stepperParams[1].motor.holdCurrent))
                Setup.write("M_TIMEOUT {}\n".format(besStr.stepperParams[1].motor.timeOut))
                Setup.write("M_LIMIT_LOW {}\n".format(besStr.stepperParams[1].motor.limitLow))
                Setup.write("M_LIMIT_HIGH {}\n".format(besStr.stepperParams[1].motor.limitHigh))
                Setup.write("M_STEPS_PER_DEGREE {}\n".format(besStr.stepperParams[1].motor.stepsPerDegree))
                Setup.write("M_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[1].motor.stepsOffset))

                Setup.write("E_STEPS_TOLERANCE {}\n".format(besStr.stepperParams[1].encoder.tolerance))
                Setup.write("E_STEPS_SET {}\n".format(besStr.stepperParams[1].encoder.stepsSet))
                Setup.write("E_STEPS_INIT {}\n".format(besStr.stepperParams[1].encoder.stepsInit))
                Setup.write("E_STEPS_RATIO {}\n".format(besStr.stepperParams[1].encoder.stepsRatio))
                Setup.write("E_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[1].encoder.stepsOffset))

                Setup.write("STEPPER_FILTER\n\n")
                Setup.write("M_STEPS_SET {}\n".format(besStr.stepperParams[2].motor.stepsSet))
                Setup.write("M_STEPS_INIT {}\n".format(besStr.stepperParams[2].motor.stepsInit))
                Setup.write("M_MAX_SPEED {}\n".format(besStr.stepperParams[2].motor.maxSpeed))
                Setup.write("M_HOLD_CURRENT {}\n".format(besStr.stepperParams[2].motor.holdCurrent))
                Setup.write("M_TIMEOUT {}\n".format(besStr.stepperParams[2].motor.timeOut))
                Setup.write("M_LIMIT_LOW {}\n".format(besStr.stepperParams[2].motor.limitLow))
                Setup.write("M_LIMIT_HIGH {}\n".format(besStr.stepperParams[2].motor.limitHigh))
                Setup.write("M_STEPS_PER_DEGREE {}\n".format(besStr.stepperParams[2].motor.stepsPerDegree))
                Setup.write("M_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[2].motor.stepsOffset))

                Setup.write("E_STEPS_TOLERANCE {}\n".format(besStr.stepperParams[2].encoder.tolerance))
                Setup.write("E_STEPS_SET {}\n".format(besStr.stepperParams[2].encoder.stepsSet))
                Setup.write("E_STEPS_INIT {}\n".format(besStr.stepperParams[2].encoder.stepsInit))
                Setup.write("E_STEPS_RATIO {}\n".format(besStr.stepperParams[2].encoder.stepsRatio))
                Setup.write("E_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[2].encoder.stepsOffset))

                Setup.write("STEPPER_LENS\n\n")
                Setup.write("M_STEPS_SET {}\n".format(besStr.stepperParams[3].motor.stepsSet))
                Setup.write("M_STEPS_INIT {}\n".format(besStr.stepperParams[3].motor.stepsInit))
                Setup.write("M_MAX_SPEED {}\n".format(besStr.stepperParams[3].motor.maxSpeed))
                Setup.write("M_HOLD_CURRENT {}\n".format(besStr.stepperParams[3].motor.holdCurrent))
                Setup.write("M_TIMEOUT {}\n".format(besStr.stepperParams[3].motor.timeOut))
                Setup.write("M_LIMIT_LOW {}\n".format(besStr.stepperParams[3].motor.limitLow))
                Setup.write("M_LIMIT_HIGH {}\n".format(besStr.stepperParams[3].motor.limitHigh))
                Setup.write("M_STEPS_PER_DEGREE {}\n".format(besStr.stepperParams[3].motor.stepsPerDegree))
                Setup.write("M_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[3].motor.stepsOffset))

                Setup.write("E_STEPS_TOLERANCE {}\n".format(besStr.stepperParams[3].encoder.tolerance))
                Setup.write("E_STEPS_SET {}\n".format(besStr.stepperParams[3].encoder.stepsSet))
                Setup.write("E_STEPS_INIT {}\n".format(besStr.stepperParams[3].encoder.stepsInit))
                Setup.write("E_STEPS_RATIO {}\n".format(besStr.stepperParams[3].encoder.stepsRatio))
                Setup.write("E_STEPS_OFFSET {}\n\n".format(besStr.stepperParams[3].encoder.stepsOffset))

                Setup.write("FILTER_HEATER\n\n")
                Setup.write("FILTER_TYPE {}\n".format(besStr.filterParams.type))
                Setup.write("TEMPERATURE {}\n".format(besStr.filterParams.temperature))
                Setup.write("TEMPERATURE_HIGH {}\n".format(besStr.filterParams.th_high))
                Setup.write("TEMPERATURE_LOW {}\n".format(besStr.filterParams.th_low))

        except:
            error=1  #can't open config file

        Setup.close()
        return error
    
if __name__ == '__main__':

    # Create an instance of PureConfigFileWrite
    fileName = "BES_settings_test.cnf"
    # pureConfigFileWrite = PureConfigFileWrite(fileName)
    # Call the writeFile method
    # error = pureConfigFileWrite.writeFile(besStr)
