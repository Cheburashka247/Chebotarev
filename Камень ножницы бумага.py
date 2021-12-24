#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     23.12.2021
# Copyright:   (c) Admin 2021
# Licence:     <your licence>
#-----------------------------------------------------------------------------
a = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}
while True:
    b = input("Игрок 1: ")
    c = input("Игрок 2: ")

    if b == c:
        print("ничья")
        continue
    for i, j in a.items():
        if b == i and c == j:
            print("Победил Игрок 1")
            break
        elif c == i and b == j:
            print("Победил Игрок 2")
            break