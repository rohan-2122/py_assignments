import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,16,5,17,29,38,25,12,22,31]
y=[55,64,57,43,46,78,54,68,98,65,34]

slope, intercept, r, p,std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)
print(speed)

mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()