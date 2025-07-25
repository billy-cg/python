print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = input("elegi una opcion(1-4):")

num1 = float(input("primer numero: "))
num2 = float(input("segundo numero: "))

if opcion == "1":
    print("resultado:", num1 + num2)
elif opcion == "2":
    print("resultado:", num1 - num2)
elif opcion == "3":
    print("resultado:", num1 * num2)
elif opcion == "4":
    if num2 != 0:
        print ("resultado:", num1 / num2)
    else: 
        print("error: division por cero.") 
else: 
    print("opcion invalida.")         