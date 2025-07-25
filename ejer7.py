nombre = input("¿como te llamas?: ")
horas = int(input("¿cuantas horas trabajaste esta semana?: "))
precio = float(input("¿cuanto ganas por hora?:$ "))

sueldo = precio * horas

print(f"hola,{nombre}, trabajastes {horas} horas y ganas ${precio}.")
print(f"tu sueldo es:${sueldo}")