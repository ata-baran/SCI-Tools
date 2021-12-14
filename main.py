"""
Scientific tools software by ata baran
"""
import scientific_calculator as sci
import area_calculator as calc
import grapher as graph
import random_generator as rgen
import data_store_creator as dtc

def sciencetific_converter():
    print("SCIENCETIFIC CONVERTER\n")

    inputtext = "Choose one of the choices between 1-9\n\n1)Lenght Units Converter\n2)Weights Units Converter\n3)Power Converter\n4)Tempereture Convereter\n5)Area Converter\n6)Volume Converter\n7)Time Converter\n8)Pressure Converter\n9)Data Storage Converter\n\nEnter Your Choice: "

    userval = int(input(inputtext))

    while True:
        if userval > 9 or userval <= 0:
            print("\nNot an option!\n")
            userval = int(input(inputtext))
        else:
            if userval == 1:
                val = float(input("\nPlease enter the value to be converted: "))
                sci.lenght(val)
            elif userval == 2:
                val2 = float(input("\nPlease enter the value to be converted: "))
                sci.weight_converter(val2)
            elif userval == 3:
                sci.power()
            elif userval == 4:
                sci.temp()
            elif userval == 5:
                sci.area()
            elif userval == 6:
                sci.volume()
            elif userval == 7:
                sci.time()
            elif userval == 8:
                sci.pressure()
            elif userval == 9:
                sci.data()
            break

def area_calculator():
    print("AREA CALCULATOR\n")

    inputtext = "Choose one of the choices between 1-4\n\n1)Sqaure\n2)Rectangle\n3)Circle\n4)Triangle\n\nEnter Your Choice: "

    userval = int(input(inputtext))

    while True:
        if userval > 4 or userval <= 0:
            print("\nNot an option!\n")
            userval = int(input(inputtext))
        else:
            if userval == 1:
                calc.sqaure()
            elif userval == 2:
                calc.rectangle()
            elif userval == 3:
                calc.circle()
            elif userval == 4:
                calc.triangle()
def grapher():
    print("GRAPHER\n")

    inputtext = "Choose one of the choices between 1-3\n\n1)Line Graph\n2)Pie Graph\n3)Bar Graph\n\nEnter Your Choice: "

    userval = int(input(inputtext))

    while True:
        if userval > 3 or userval <= 0:
            print("\nNot an option!\n")
            userval = int(input(inputtext))
        else:
            if userval == 1:
                graph.line()
            elif userval == 2:
                graph.pie()
            elif userval == 3:
                graph.bar()

def random_generator():
    print("RANDOM GENERATOR\n")

    inputtext = "Choose one of the submenus between 1-4\n\n1)Integers\n2)Floats\n3)ArrayGenerator\n4)2D array generator\n\nEnter Choice: "

    userval = int(input(inputtext))

    while True:
        if userval > 4 or userval <= 0:
            print("\nNot an option!\n")
            userval = int(input(inputtext))
        else:
            if userval == 1:
                rgen.int()
            elif userval == 2:
                rgen.float()
            elif userval == 3:
                rgen.array()
            elif userval == 4:
                rgen.twoarray()
            break

def data_store_creator():
    print("DATA STORE CREATOR\n")

    inputtext = "Choose one of the submenus 1 or 2\n\n1)Sciencetific Dictonary\n2)Sciencetific Abravations\n\nEnter Choice: "

    userval = int(input(inputtext))

    while True:
        if userval > 2 or userval <= 0:
            print("\nNot an option!\n")
            userval = int(input(inputtext))
        else:
            if userval == 1:
                dtc.dic()
            elif userval == 2:
                dtc.abr()
            break



print("SCIENTIFIC TOOLS SOFTWARE \n")

inputtext = "Choose one of the submenus between 1-5\n\n1)Scientific Coverter\n2)Area Calculator\n3)Grapher\n4)Random Generator\n5)Data Store Creator\n\nEnter Choice: "

userval = int(input(inputtext))

while True:
    if userval > 5 or userval <= 0:
        print("\nNot an option!\n")
        userval = int(input(inputtext))
    else:
        if userval == 1:
            sciencetific_converter()
        elif userval == 2:
            area_calculator()
        elif userval == 3:
            grapher()
        elif userval == 4:
            random_generator()
        elif userval == 5:
            data_store_creator()
        break


