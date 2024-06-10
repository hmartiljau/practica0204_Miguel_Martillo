productos = {'Pan': 1.40, 'Huevos': 2.30, 'Cebolla': 0.85, 'Aceite': 4.35}

producto = input('¿Qué producto quieres? ').title()
cantidad = float(input('¿Cuántos unidades quiere? '))

if producto in productos:
    print(cantidad, 'unidades de', producto, 'cuestan', productos[producto] * cantidad, '€')
else:
    print("Lo sienton no nos quedan mas de ", producto)