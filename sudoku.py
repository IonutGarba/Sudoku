import os


def color_text(code):
    return "\33[31m{code}".format(code=code)


def tabla_de_sudoku():
    matrice = []
    for i in range(0, 9):
        linie = []
        for j in range(0, 9):
            linie += [0]
        matrice += [linie]
    return matrice


def afisare(lista):
    print(end="                                              ")
    for i in range(0, len(lista)):
        if i % 3 == 0:
            print(end=" ")
        print(color_text(lista[i]), end=" ")
    print()  # printeaza o linie noua


def afisare_tabla(matrice):
    print("\n\n\n\n")
    for i in range(0, 9):
        if i % 3 == 0:
            print()
        afisare(matrice[i])

    print()


def inserteaza_valoare_citita():
    linie = int(input("Linie : "))
    coloana = int(input("Coloana: "))
    valoare = int(input("Valoare: "))
    inserteaza_valoare(linie, coloana, valoare)


def inserteaza_valoare(linie, coloana, valoare):
    global tabla
    if valoare <= 9 and valoare >= 1:
        tabla[linie][coloana] = valoare


def final_joc():
    global tabla
    for i in range(0, 9):
        for j in range(0, 9):
            if tabla[i][j] == 0:
                return False
    return True


def umple():
    global tabla
    for i in range(0, 9):
        for j in range(0, 9):
            tabla[i][j] += 1
    tabla[0][0] = 0


def tabla_valida():
    for z in range(0, 9):
        for i in range(0, 8):
            for j in range(i + 1, 9):
                if tabla[z][i] == tabla[z][j] and tabla[z][i] != 0:
                    return False

    for z in range(0, 9):
        for i in range(0, 8):
            for j in range(i + 1, 9):
                if tabla[i][z] == tabla[j][z] and tabla[i][z] != 0:
                    return False
    return True


os.system("color")
tabla = tabla_de_sudoku()
afisare_tabla(tabla)

while (not final_joc()):
    inserteaza_valoare_citita()
    os.system('cls')
    afisare_tabla(tabla)

if tabla_valida():
    print("Bravo, ai castigat!")
else:
    print("Nasol, ai pierdut...")