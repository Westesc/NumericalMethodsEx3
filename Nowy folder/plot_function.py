import matplotlib.pyplot as plt
from typing import List

def ploting2(x: List[float], y: List[float], tabx: List[float], taby: List[float],function:object):
    y_original=[]
    for i in x:
        y_original.append(function.value(i))
    plt.plot(x,y_original,c='#aee33b',label='orginal')
    plt.plot(x, y,label='interpolation')
    plt.scatter(tabx, taby, c='#8a134e',label='punkty interpolacji')
    plt.legend()
    plt.show()
def ploting(x: List[float], y: List[float], tabx: List[float], taby: List[float]):
    plt.plot(x, y,label='interpolation')
    plt.scatter(tabx, taby, c='#8a134e',label='punkty interpolacji')
    plt.legend()
    plt.show()