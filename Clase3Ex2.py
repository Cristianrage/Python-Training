#En base al gasto total en un restaurante, calcular la propina, preguntar
#al cliente que porcentaje de propina piensa dejar

subtotal = float(input("Ingrese cuanto gasto: "))
porc_propina = int(input("Ingrese el porcentaje de propina que desea dejar: "))

propina = subtotal * (porc_propina / 100)
total = subtotal + propina

print(f"El total de su cuenta es {total} compuesto por un gasto de {subtotal} \n y una propina de {propina}")