#!/usr/bin/env python
"""
Je aangepaste rekenmachine die nu volledig aangepast/verbeterd is met de juiste imports, functies en flowcontrol
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def optellen(x, y): #to declare the add function
    return x + y    #to add numbers x and y


def aftrekken(x, y): #to declare the subtract function
    return x - y     #to subtract numbers x and y


def vermenigvuldigen(x, y): #to declare the multiply function
    return x * y            #to multiply numbers x and y


def delen(x,y):     #to declare the divide function
    return x / y    #to divide numbers x and y


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("REKENMACHINE, GEMAAKT DOOR SENNE")  #to print the program title
    print("Kies wat je wilt doen")             #to print the calculation choices:
    print("1: optellen")
    print("2: aftrekken")
    print("3: vermenigvuldigen")
    print("4: delen")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        keuze = input("Vul je keuze in  (1/2/3/4):\n")           #to prompt the choice to the user

        if keuze in ('1', '2', '3', '4'):                       #to determine whether the choice is possible
            getal1 = int(input("Geef het eerste getal in:\n"))   #to ask for the first number
            getal2 = int(input("Geef het tweede getal in:\n"))   #to ask for the second number

            if keuze == '1':                                                #to add the numbers
                print(getal1, "+", getal2, "=", optellen(getal1, getal2))   #to print the result
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif keuze == '2':                                              #to subtract the numbers
                print(getal1, "-", getal2, "=", aftrekken(getal1, getal2))  #to print the result
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif keuze == '3':                                                      #to multiply the numbers
                print(getal1, "*", getal2, "=", vermenigvuldigen(getal1, getal2))   #to print the result
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif keuze == '4':                                          #to divide the numbers
                print(getal1, "/", getal2, "=", delen(getal1, getal2))  #to print the result
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            break
        else:
            print("Ongeldige invoer")  #to say that the choice is invalid


if __name__ == '__main__':
    main()
    optellen()
    aftrekken()
    delen()
    vermenigvuldigen()