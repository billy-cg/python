total_gastado = 0
total_ahorrado = 0 
productos = []
contador_productos = 0

while True:
    nombre = input("nombre del producto: ")
    precio = float(input("precio:$"))
    descuento = float(input("descuento:%"))

    descuento_enPesos = (descuento * precio)/100
    precio_conDescuento = precio - descuento_enPesos

    #acumulador 
    total_gastado += precio_conDescuento
    total_ahorrado += descuento_enPesos
    contador_productos += 1
    productos.append((nombre, precio_conDescuento, descuento_enPesos))

    print(f"producto: {nombre}")
    print(f"descuento en pesos:${descuento_enPesos:.2f}")
    print(f"precio final con descuento:${precio_conDescuento:.2f}")

    continuar = input("¿queres ingresar otro pruducto? (s/n):").lower()
    if continuar != "s":
        break
    #resumen final

    print("\n------RESUMEN FINAL------")
    for i, (nombre, final, ahorro) in enumerate(productos, start=1):
       print(f"{i}. {nombre} → Final: ${final:.2f}, Ahorro: ${ahorro:.2f}")

print(f"\nCantidad total de productos: {contador_productos}")
print(f"Total gastado: ${total_gastado:.2f}")
print(f"Total ahorrado: ${total_ahorrado:.2f}")
print("---------------------------")