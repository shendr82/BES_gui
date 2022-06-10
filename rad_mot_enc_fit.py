# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:32:11 2022

@author: ShendR
"""
import numpy as np
# from numpy import arange
#from pandas import read_csv
from scipy.optimize import curve_fit
# from matplotlib import pyplot


    # Polynomial function definition
def objective(x, a, b, c, d):
    return a * x**3 + b * x ** 2 + c*x +d
def value_m(x, a, b, c, d):
    y=a * x**3 + b * x ** 2 + c*x +d
    return y


            # Mirror  
def mirror_fit(x=1.35):
    
    # Motor
    radius = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
    motor = np.array([26200, 41000, 50000, 57500, 65900, 74000, 83800, 93000, 102400, 112000])
    
    popt, _ = curve_fit(objective, radius, motor)
    a, b, c, d = popt
    
    # x=1.2
    y=value_m(x, a, b, c, d)
        
        # Encoder
    encoder = np.array([-909,-1430, -1745, -2007, -2303, -2587, -2933, -3256, -3585, -3925])
    popt2, _ = curve_fit(objective, radius, encoder)
    e, f, g, h = popt2
    y_enc = value_m(x, e, f, g, h)
    
    return[y,a, b , c, d, y_enc, e, f, g, h]

# mirror_fit1 = mirror_fit()
# print(f'Mirror motor value: {mirror_fit1[0]}')
# print(f'Mirror encoder value: {mirror_fit1[5]}')


            # Camera  
def camera_fit(x=1.35):
    
    # Motor
    radius = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
    motor = np.array([24500, 21500, 19750, 18500, 17000, 15500, 13000, 11500, 9300, 7200])
    
    popt, _ = curve_fit(objective, radius, motor)
    a, b, c, d = popt
    
    # x=1.2
    y=value_m(x, a, b, c, d)
        
        # Encoder
    encoder = np.array([-3920,-3438, -3160, -2960, -2719, -2480, -2080, -1840, -1498, -1152])
    popt2, _ = curve_fit(objective, radius, encoder)
    e, f, g, h = popt2
    y_enc = value_m(x, e, f, g, h)
    
    return[y,a, b , c, d, y_enc, e, f, g, h]

# camera_fit1 = camera_fit()
# print(f'Camera motor value: {camera_fit1[0]}')
# print(f'Camera encoder value: {camera_fit1[5]}')


            # Lens 
def lens_fit(x=1.35):
    
    # Motor
    radius = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
    motor = np.array([123000, 123000, 100000, 80000, 60000, 50000, 42000, 35000, 15000, 0])
    
    popt, _ = curve_fit(objective, radius, motor)
    a, b, c, d = popt
    
    # x=1.2
    y=value_m(x, a, b, c, d)
        
        # Encoder
    encoder = np.array([-19680, -19680, -16002, -12803, -9601, -8002, -6720, -5599, -2401, 	0])
    popt2, _ = curve_fit(objective, radius, encoder)
    e, f, g, h = popt2
    y_enc = value_m(x, e, f, g, h)
    
    return[y,a, b , c, d, y_enc, e, f, g, h]

# lens_fit1 = lens_fit()
# print(f'Lens motor value: {lens_fit1[0]}')
# print(f'Lens encoder value: {lens_fit1[5]}')

        
    