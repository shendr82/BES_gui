# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:37:47 2023

@author: ShendR
"""

class CnfStructure:
    def __init__(self):
        self.besStr = self.BESStr()
       
    class FilterHeaterParams:
        def __init__(self):
            self.type = ''
            self.temperature = 0

    class Encoder:
        def __init__(self):
            self.tolerance = 0
            self.stepsSet = 0
            self.stepsInit = 0
            self.stepsRatio = 0.0
            self.stepsOffset = 0

    class Motor:
        def __init__(self):
            self.stepsSet = 0
            self.stepsInit = 0
            self.maxSpeed = 0
            self.holdCurrent = 0
            self.timeOut = 0
            self.limitLow = 0
            self.limitHigh = 0
            self.stepsPerDegree = 0.0
            self.stepsOffset = 0

    class StepperParams:
        def __init__(self):
            self.viewRadius = 0.0
            self.mirrorAngle = 0.0
            self.motor = CnfStructure.Motor()
            self.encoder = CnfStructure.Encoder()

    class ADPCAMParams:
        def __init__(self):
            self.rate = 0
            self.duration = 0.0
            self.start = 0.0
            self.apd_bias1 = 0
            self.apd_bias2 = 0
            self.temperature = 0
            self.trigDelay = 0.0
            self.clkSrc = 0
            self.stream_if = ''

    class BESStr:
        def __init__(self):
            self.apdParams = CnfStructure.ADPCAMParams()
            self.stepperParams = [CnfStructure.StepperParams() for _ in range(4)]
            self.filterParams = CnfStructure.FilterHeaterParams()
