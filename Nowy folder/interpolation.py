from typing import List

def f(j:int,tabx:List[float],x:float,number:int)->float:
    resault:float = 1
    for i in range(number):
        if i != j:
            resault *= (x - tabx[i])
    return float(resault)
def a(j:int,tabx:List[float],taby:List[float],number:int)->float:
    return taby[j]/f(j,tabx,tabx[j],number)

def interpol(x:float,tabx:List[float],taby:List[float]) -> float:
    result = 0
    number = len(tabx)
    for i in range(number):
        result += a(i,tabx,taby,number) * f(i,tabx,x,number)
    return result