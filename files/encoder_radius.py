# fit a second degree polynomial to the economic data
import numpy as np
from numpy import arange
#from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot


# define the true objective function
def objective(x, a, b, c, d):
    return a * x**3 + b * x ** 2 + c*x +d
def value_m(x, a, b, c, d):
    y=a * x + b * x ** 2 + c*x**3 +d
    return y

# load the dataset
r=np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
r_1=np.array([0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])

e_1=np.array([-909,-1430, -1745, -2007, -2303, -2587, -2933, -3256, -3585, -3925])
e_M=np.array([-906,-1427, -1743, -2010, -2303,-2588, -2932, -3257, -3586, -3928])
e_C=np.array([-3920,-3438, -3160, -2960, -2719, -2480, -2080, -1840, -1498, -1152])
e_L=np.array([-19680, -19680, -16002, -12803, -9601, -8002, -6720, -5599, -2401, 	0])
e_L_1=np.array([ -19680, -16002, -12803, -9601, -8002, -6720, -5599])

x=r
y=e_M
def y_e_abs(y):
    x_array=[]
    for i in y:
        if int(i)<0:
            x_array.append(-1*i)
        else:
            x_array.append(i)
    return x_array



# curve fit
popt, _ = curve_fit(objective, x, y_e_abs(y))
# summarize the parameter values
a, b, c, d = popt
print('y= %.1f * x**3 + %.1f * x**2 + %.1f*x+ %.1f' % (a, b, c, d))
# plot input vs output
pyplot.scatter(x, y_e_abs(y))
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 0.05)

x=1.5
print("Ha x értéke ", x, "akkor y értéke", value_m(x, a, b,c, d))



# calculate the output for the range
y_line = objective(x_line, a, b, c, d)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
