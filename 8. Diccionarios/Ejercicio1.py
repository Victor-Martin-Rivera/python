# En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

# {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid", "El Salvador" : "San Salvador"}

pais = input("Ingresa un pais para conocer su capital: ")

#Convierte la letra en mayuscula (de capital) y el in se asegura de que un metodo este dentro del diccionario
if pais.title() in diccionario :
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra en el diccionario")