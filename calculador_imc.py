#pylint:disable=E0401

import time
from os import *
from tabulate import tabulate

data = [
    ["Por debajo de 18.5", "Bajo peso"],
    ["18.5 - 24.9", "Peso normal"],
    ["25.5 - 29.9", "Pre-obesidad o Sobrepeso"],
    ["30.0 - 34.9", "Obesidad clase I"],
    ["Por encima de 35.5", "Obesidad clase II"],
    ["Por encima de 40", "Obesidad clase III"]
]

table = tabulate(data, headers=["IMC", "ESTADO"], tablefmt="grid")


while True:    
    print(table)
    masa_corporal = input("\nIngrese La Masa Corporal Kg: ")
    
    if masa_corporal.isdigit() == True:
        estatura = input("\nIngrese La Estatura: ")
        
        if "." in estatura:
         
            IMC = int(masa_corporal) /  (float(estatura) ** 2)
            IMC = round(IMC,1)
            if 18.5 > IMC:
    	        print(f"\n{IMC} : Bajo Peso")
	
            elif 18.5 <= IMC and 24.9 >= IMC:
            	print(f"\n{IMC} : Probesidad o Sobrepeso")

            elif 25.0 <= IMC and 29.9 >= IMC:
            	print(f"\n{IMC} : Obesidad I")

            elif 30.0 <= IMC and 34.9 >= IMC:
            	print(f"\n{IMC} : Obesidad II")
            	
	
            elif 35.0 <= IMC and 39.9 <= IMC:
            	print(f"\n{IMC} : Obesidad III")
             
            input("\nPresiona Enter !")
            system("clear")
                  
        else:
            print("\nError al ingresar la ESTATURA\n")
            time.sleep(1)
            system("clear")

	
    else:
        print("\nError al ingresar la MASA\n")
        time.sleep(1)
        system("clear")    	
