nombre = input('¿Cual es tu nombre? ')
edad = input('¿Dime tu edad? ')
direccion = input('¿Cual es tu direccion? ')
telefono = input('¿Cuál es tu numero de telefono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 
      'y su numero de telefono es', persona['telefono'])