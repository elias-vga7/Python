from datetime import datetime
import time

time1 = time.time()
time2 = time.localtime(time1)
time3 = time.asctime(time2)                       # datetime.srftdate(datetime.now(), "%c")

print(time1)
print(time2)
print(time2.tm_year)
print(time3)
print("")

###################################################################################

dt1 = datetime.now()
print(f"Fecha 1: {dt1}")

print("Dia: ", str(dt1.day).zfill(2))
print("Mes: ", str(dt1.month).zfill(2))
print("Año: ", dt1.year)
print("Hora: ", dt1.hour)
print("Minutos: ", dt1.minute)
print("Segundos: ", dt1.second)
print("Milisegundos: ", dt1.microsecond)
print("")

dt2 = datetime.now().date()
print("Fecha 2: ", dt2)

print("Dia: ", dt2.day)
print("Mes: ", dt2.month)
print("Año: ", dt2.year)
print("")

##################################################################3
# Parse Fechas

strfecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(strfecha, "%d-%m-%Y").date()

print(f"Fecha de nacimiento: {dt3}")
print("Fecha de nacimiento:", dt3.strftime("%A, %d-%B-%Y"))

print(f"Edad: {dt2.year-dt3.year}")

dias = dt2 - dt3
print(f"Has vivido {dias} dias.")


