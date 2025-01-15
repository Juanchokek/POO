# pide la edad de Juan
EdadJuan = float(input("Ingrese la edad de Juan: "))

# calculamos edades y las redondeamos a un valor entero
EdadAlberto = round((2/3) * EdadJuan)
EdadAna = round((4/3) * EdadJuan)
EdadMama = round(EdadJuan + EdadAlberto + EdadAna)

# imprimimos los resultados
print("Edad de Juan: " + str(round(EdadJuan)))
print("Edad de Alberto: " + str(EdadAlberto))
print("Edad de Ana: " + str(EdadAna))
print("Edad de la mamá: " + str(EdadMama))