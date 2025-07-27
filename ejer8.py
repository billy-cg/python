nombre = input("nombre del producto: ")
precio = float(input("precio:$"))
descuento = float(input("descuento:%") )

descuento_enPesos = (descuento * precio)/100
precio_conDescuento = precio - descuento_enPesos

print(f"Producto: {nombre}")
print(f"Descuento en pesos: ${descuento_enPesos:.2f}")
print(f"Precio final con descuento: ${precio_conDescuento:.2f}")