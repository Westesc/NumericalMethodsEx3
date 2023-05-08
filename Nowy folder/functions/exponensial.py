from numpy import float_power
from typing import List
from helpers import powii, powfi, powff

class exponensial:
    exponensial_values: List[int]
    a:float
    b:float
    def __init__(self):
        print("Funkcja wykładnicza ma postać f(x)=a^x+b")
        self.a = float(input("Podaj wartość a: "))
        self.b = float(input("Podaj wartość b: "))

    def value(self, x) -> float:

        if isinstance(self.a, int):
            if isinstance(x, int):
                return powii(self.a, x) + self.b
            else:
                return powff(self.a, x) + self.b
        else:
            if isinstance(x, float):
                return powff(self.a, x) + self.b
            else:
                return powfi(self.a, x) + self.b
        