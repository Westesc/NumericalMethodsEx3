from typing import List

from functions.polynomial import polynomial
from functions.exponensial import exponensial
from functions.trigonometric import trigonometric
from functions.modulo import modulo

text_select_upper_function: str = "Wybierz funkcję nadrzędną (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Modulo): "
text_select_lower_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Modulo, 5.Złożona): "

class combination:
    def __init__(self):
        self.function1_type = int(input(text_select_upper_function))

        match self.function1_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function1 = polynomial()
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function1 = trigonometric()
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function1 = exponensial()
            case 4:
                print("Wybrano funckje typu modulo.")
                self.function1 = modulo()
            case other:
                return
            
        self.function2_type = int(input(text_select_lower_function))

        match self.function2_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function2 = polynomial()
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function2 = trigonometric()
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function2 = exponensial()
            case 4:
                print("Wybrano funckje typu modulo.")
                self.function1 = modulo()
            case 5:
                print("Wybrano funckje typu złożona.")
                self.function2 = combination()
            case other:
                return

    def value(self,x) -> float:
        return self.function1.value(self.function2.value(x))