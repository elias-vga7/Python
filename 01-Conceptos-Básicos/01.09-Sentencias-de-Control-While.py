valor = 0

while (valor < 5):
    valor = valor + 1                                                # equivalente a valor += 1
    if(valor == 2):
        break
    print(f"El valor es {valor}.")

print("Fin del WHILE")
print("")

# Número de elementos/valores: 8
# Posiciones 0 hasta num elementos -1 (0-7)

friends = ["Efraín", "Tato", "Ariel", "Hugo", "Marcos", "Luci", "Natalia", "Meli"]  
posicion = 0

while (posicion < len(friends)):
    print(f"{friends[posicion]}")
    posicion += 1
else:
    print("Else del WHILE")
    
print("Fin de Lista WHILE")


# Simulación Do-While:
#while(true):
    #sentencias
    #if (posicion < len(friends)):
     #   break
#else:
    #print("Else del WHILE") """ 
