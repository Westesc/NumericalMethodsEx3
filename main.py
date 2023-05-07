from functions.trigonometric import trigonometric
from functions.exponensial import exponensial
from functions.polynomial import polynomial
from functions.combination import combination
from interpolation import interpol
import plot_function

text_error_wrong_input: str = "Wprowadzono błędny znak nie odpowiadający poleceniu!"
text_select_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Złożona): "


def main():
    print("Program oblicza interpolacje przy pomocy metody Lagrange'a dla nierównych odstępów argumentu")
    wybor = int(input("Wybierz czy program ma wziać wartosći 1)z pliku czy 2)po przez funkcje"))
    tabx = []
    taby = []
    function: object
    match wybor:
        case 1:
            with open("data.txt", "r") as file:
                for line in file:
                    l = line.strip().split("|")
                    for i, v in enumerate(l):
                        if i % 2 == 0:
                            tabx.append(float(v))
                        else:
                            taby.append(float(v))

        case 2:
            function_type = int(input(text_select_function))
            match function_type:
                case 1:
                    print("Wybrano funckje typu wielomian.")
                    function = polynomial()
                case 2:
                    print("Wybrano funckje typu trygonometryczna.")
                    function = trigonometric()
                case 3:
                    print("Wybrano funckje typu wykładnicza.")
                    function = exponensial()
                case 4:
                    print("Wybrano funckje typu złożona.")
                    function = combination()
                case other:
                    print(text_error_wrong_input)
                    return
            nodes = int(input("Podaj ilość węzłów:"))
            for i in range(nodes):
                x = float(input("Podaj wartość %d x:" % (i + 1)))
                tabx.append(x)
                taby.append(function.value(x))
        case other:
            print(text_error_wrong_input)
            return

    start = float(input("Podaj początek przedziału:"))
    end = float(input("Podaj koniec przedziału:"))
    if end < start:
        tmp = start
        start = end
        end = tmp
    step = (end - start) / 2000
    x = start
    tabx2 = []
    taby2 = []
    while x < end:
        tabx2.append(x)
        x = x + step
        taby2.append(interpol(x, tabx, taby))
    if wybor ==1:
        plot_function.ploting(tabx2, taby2, tabx, taby)
    else:
        plot_function.ploting2(tabx2, taby2, tabx, taby, function)


if __name__ == '__main__':
    main()
