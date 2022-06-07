# fit a second degree polynomial to the economic data
import numpy as np
from numpy import arange
#from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot


# define the true objective function
def objective_2(x, a, b):
    return a * x + b
def value_em(x, a, b):
    y=a * x + b
    return y

# load the dataset
e_1=np.array([-909,-1430, -1745, -2007, -2303, -2587, -2933, -3256, -3585, -3925])
e_M=np.array([-906,-1427, -1743, -2010, -2303,-2588, -2932, -3257, -3586, -3928])
e_C=np.array([-3920,-3438, -3160, -2960, -2719, -2480, -2080, -1840, -1498, -1152])
e_L=np.array([-19680, -19680, -16002, -12803, -9601, -8002, -6720, -5599, -2401, 	0])

m_1=np.array([26200, 41000, 50000, 57500, 65900, 74000, 83800, 93000, 102400, 112000])
m_M=np.array([26200, 41000, 50000, 57500, 65900, 74000, 83800, 93000, 102400, 112000])
m_C=np.array([24500, 21500, 19750, 18500, 17000, 15500, 13000, 11500, 9300, 7200])
m_L=np.array([123000, 123000, 100000, 80000, 60000, 50000, 42000, 35000, 15000, 0])

x_e=e_C
y=m_C

def x_e_abs(x_e):
    x_array=[]
    for i in x_e:
        if int(i)<0:
            x_array.append(-1*i)
        else:
            x_array.append(i)
    return x_array


# define the true objective function


popt, _ = curve_fit(objective_2, x_e_abs(x_e), y)
# summarize the parameter values
a, b = popt
print('y = %.2f * x + %.2f' % (a, b))
# plot input vs output
pyplot.scatter(x_e_abs(x_e), y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x_e_abs(x_e)), max(x_e_abs(x_e)), 1)
# calculate the output for the range
y_line = objective_2(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
# choose the input and output variables