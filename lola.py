nombre=input("cual es su nombre?: ")
print("hola", nombre, ", crea una contraseña")
contraseña= input("cree una contraseña: ")

ingresar= input("desea ingresar? si/no: ")

if ingresar=="si":
    clave=input("ingrese su contraseña: ")
    if clave==contraseña:
        print("se ingreso correctamente")
    else:
        print ("la contraseña es incorrecta")

else:
    print("cerrando sitio")