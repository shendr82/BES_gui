#!/usr/bin/env python


### import relevant packages
import numpy as np
import serial
import time
from scipy.interpolate import interp1d

### needed for making ser objects
baudrate = 57600
timeout = 1
motorDict = {"1": 0, "3": 2, "4": 3, "mirror": 0, "camera": 2, "lens": 3}
Rarr = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])


### functions
def makeobj(motor):
    """
    Creates the Serial object to control the motors.

    Parameters
    ----------
    motor : string (or int)
        Defines what motor to make the object for. Needs to be a recognised
        key in motorDict: 1, 3, 4, mirror, camera, or lens.

    Returns
    -------
    mobject : motor object (serial.serialposix.Serial)
        The object that is used to control the motor.
    """
    try:
        mobject = serial.Serial('/dev/ttyr0{}'.format(motorDict[str(motor)]),
                  baudrate=baudrate, timeout=timeout)
        readpos(mobject, motor=motor)
    except KeyError:
        print('motor not understood, must be one of ')
        print(motorDict.keys())
        mobject = None
    return mobject


def readpos(mobject, motor=None):
    """
    Reads the current encoder position of the motor.

    Parameters
    ----------
    mobject : motor object
        The object of the motor in question.
    motor : string, optional
        A string that is added to the printout statement of the encoder
        position.
    """
    if motor is None:
        motor = ''
    mobject.write(b'01ep?\n')
    print(motor, 'encoder position is ', mobject.readline())
    return


def find_nearest(arr, val):
    """
    Find the index of an array that is closest to a specified value.

    Parameters
    ----------
    arr : array_like
        Array to find element in.
    val : number (integer or float)
        The value to find in the array.

    Returns
    -------
    result : integer
        The index in the array closest to the value.
    """
    return np.abs(arr - val).argmin()

def calibration(R):
    """
    Return the different motor positions for specified radius

    Parameters
    ----------
    R : float_like
        Major radius position to move the motors to.

    Returns
    -------
    mint : integer
        mint : The stepper motor position for the mirror.
    cint : integer
        mint : The stepper motor position for the camera.
    lint : integer
        mint : The stepper motor position for the lens.
    """
    mirrorCal = np.array([26200, 41000, 50000, 57500, 65900,
                 74000, 83800, 93000, 102400, 112000])
    cameraCal = np.array([24500, 21500, 19750, 18500, 17000,
                 15500, 13000, 11500, 9300, 7200])
    lensCal = np.array([123000, 123000, 100000, 80000, 60000,
                 50000, 42000, 35000, 15000, 0])
    if R < Rarr[0]:
        print('R is too low (below 0.7m)')
        print('setting R to 0.7m')
        R = 0.7
    elif R > Rarr[-1]:
        print('R is too high (above 1.6m)')
        print('setting R to 1.6m')
        R = 1.6
    if np.isclose(Rarr, R).any() and np.isclose(R, Rarr).any():
        ind = find_nearest(Rarr, R)
        mint = int(mirrorCal[ind])
        cint = int(cameraCal[ind])
        lint = int(lensCal[ind])
    else:
        mint = int(interp1d(Rarr, mirrorCal, kind='cubic')(R))
        cint = int(interp1d(Rarr, cameraCal, kind='cubic')(R))
        if R > 0.8:
            lint = int(interp1d(Rarr, lensCal, kind='cubic')(R))
        else:
            lint = int(lensCal[0])
    return mint, cint, lint

def checkmove(mobject):
    """
    Function that checks every second if the specified motor
    is moving. This function returns nothing but is returned
    out of once the motor has finished moving.

    Parameters
    ----------
    mobject : motor object (serial.serialposix.Serial)
        The object that is used to control the motor.

    Returns
    -------
    """
    mobject.write(b'01mv?\n')
    while not "not move" in str(mobject.readline()):
        time.sleep(1)
        mobject.write(b'01mv?\n')
    return

def gohome(mobject, motor=None, check=True, prnt=True):
    """
    Tells a specified motor to go to the home position.

    Parameters
    ----------
    mobject : motor object (serial.serialposix.Serial)
        The object that is used to control the motor.
    motor : string (optional)
        A string that is printed out describing which motor
        is being sent home. Default option is None.
    check : boolean (optional)
        A boolean that tells the function whether to check if
        the motor is moving or not. Default option is True.
    prnt : boolean (optional)
        A boolean that tells the function whether to print out
        the start and end of the motor moving or not. Default
        option is True.

    Returns
    -------
    """
    if motor is None:
        motor = ''
    if prnt:
        print(motor, 'going home')
    mobject.write(b'01gh\n')
    mobject.readline()
    if check:
        checkmove(mobject)
    if prnt:
        print(motor, 'gone home')
    return

def moveMotor(mobject, num, motor=None, home=True, check=True, prnt=True):
    if motor is None:
        motor = ''
    readpos(mobject, motor=motor)
    if home:
        gohome(mobject, motor=motor, check=check, prnt=prnt)
    if prnt:
        print('moving ', motor)
    mobject.write(bytes('01dp={}\n'.format(num), 'utf-8'))
    mobject.readline()
    mobject.write(b'01mp\n')
    mobject.readline()
    if check:
        checkmove(mobject)
        readpos(mobject, motor=motor)
    if prnt:
        print('moved ', motor)
    return

def moveRadius(R):
    mint, cint, lint = calibration(R)
    mobject = makeobj('mirror')
    cobject = makeobj('camera')
    lobject = makeobj('lens')
    # send them all home
    print('sending motors home')
    gohome(mobject, motor=None, check=False, prnt=False)
    gohome(cobject, motor=None, check=False, prnt=False)
    gohome(lobject, motor=None, check=False, prnt=False)
    # check if mirros have gone home
    checkmove(mobject)
    print('mirror has gone home')
    checkmove(cobject)
    print('camera has gone home')
    checkmove(lobject)
    print('lens has gone home')
    # move mirrors to final position
    print('moving all motors to required position')
    moveMotor(mobject, mint, motor='mirror',
              home=False, check=False, prnt=False)
    moveMotor(cobject, cint, motor='camera',
              home=False, check=False, prnt=False)
    moveMotor(lobject, lint, motor='lens',
              home=False, check=False, prnt=False)
    checkmove(mobject)
    readpos(mobject, motor='mirror')
    print('mirror has been moved')
    checkmove(cobject)
    readpos(cobject, motor='camera')
    print('camera has been moved')
    checkmove(lobject)
    readpos(lobject, motor='lens')
    print('lens has been moved')
    print('##### all motors moved #####')
    return

# def moveRadius(R):
#     if not np.isclose(R, [0.7, 0.8, 0.9, 1.0, 1.1,
#                       1.2, 1.3, 1.4, 1.5, 1.6]).any():
#         print('R is not one of the calibrated positions')
#         print('Must specify a calibrated R or move mirrors independantly')
#         return
#     mint, cint, lint = calibration(R)
#     mobject = makeobj('mirror')
#     print('moving mirror')
#     moveMotor(mobject, mint, motor='mirror')
#     print('mirror moved')
#     mobject = makeobj('camera')
#     print('moving camera')
#     moveMotor(mobject, cint, motor='camera')
#     print('camera moved')
#     mobject = makeobj('lens')
#     print('moving lens')
#     moveMotor(mobject, lint, motor='lens')
#     print('lens moved')
#     return

#
