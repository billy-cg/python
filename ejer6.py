from datetime import date

nacimiento = int(input("ingresa el año en que naciste: "))

año_actual = date.today().year

edad = año_actual - nacimiento

print(f"tenes {edad} años.")