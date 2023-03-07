import sys

num1 = 0
num2 = 100

try:
    #raise ValueError("Mi error")
    num3 = num2 / num1
    print(f"Resultado: {num3}")
    f = open('myfile.txt')
except ZeroDivisionError as err:
    print("Vaya! No se puede dividir por cero")
    print(err)
    print(type(err))
except FileNotFoundError as err:
    print("Vaya! El fichero no existe")
    print(err)
    print(type(err))
except Exception as err:
    print("Vaya! Se ha producido un error")
    print(err)
    print(type(err))
finally:
    print("Bloque FINALLY")

print("Fin")

