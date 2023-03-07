for m in range(0, 100, 7):
    print(f"Número {m}")


friends = ["Efraín", "Tato", "Ariel", "Hugo", "Marcos", "Luci", "Natalia", "Meli"]     # Colección

print(friends)                                               # Recorrido en colección
print(friends[0])
print(f"Número de amigos: {len(friends)}")
print("")

for m in range(0, 7, 1):                                     # Valor estatico final   
    print(f"{m}: {friends[m]}")
print("")

for m in range(0, len(friends), 1):                          # Valor que toma todos los elementos de la coleccion por len
    print(f"{m}: {friends[m]}")
    print("")

for m in friends:                                            # No nos muestra la posición de cada elemento de la colección
    print(f"{m}")
print("")

#############################################################################################
# CONTINUE / BREAK

for m in range(0, 20, 1):
    print(f"Número: {m} - Inicio")
    if (m == 10):
        continue
    print(f"Número: {m} - Fin")


for m in range(0, 20, 1):
    print(f"Número: {m} - Inicio")
    if (m == 10):
        break
    print(f"Número: {m} - Fin")
print("")


for m in friends:
    if (m == "Hugo"):
        continue
    print(f"{m}")
print("")

for m in friends:
    if (m == "Hugo"):
        break
    print(f"{m}")
print("")
