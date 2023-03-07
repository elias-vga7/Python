cadena = "twenty one pilots"

print(cadena)
print(cadena[3])
print(cadena[3:])
print(cadena[:7])
print(cadena[3:7])
print(cadena[-1])
print(len(cadena))
print("")

print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o", "ø"))
print(cadena.isdigit())
print("57".isdigit())
print(cadena.count("w"))

# Formateando Cadenas

mensaje = " and so are you."

print(mensaje)
print("We are twenty one pilots " + mensaje)
print("We are twenty one pilots {}".format(mensaje))
print("We are twenty one pilots {n}".format(n=mensaje))
print("We are twenty one pilots {mensaje}")
print(f"We are twenty one pilots {mensaje}")
print("")

resultado = "We are twenty one pilots {n}".format(n=mensaje)
print(resultado)
print("")

# Formateo con números
numero = 10 / 3
print(numero)
print("Número: {n}".format(n=numero))
print("Número: {}".format(numero))
print("Número: {n:1.2f}".format(n=numero)) 
      




