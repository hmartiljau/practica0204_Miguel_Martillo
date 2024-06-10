monedas = {'euro': '€', 'dollar': '$', 'yen': '¥'}
moneda = input("Introduce una divisa: ").lower()
if moneda in monedas:
    print(monedas[moneda])
else:
    print("La divisa no está.")
    