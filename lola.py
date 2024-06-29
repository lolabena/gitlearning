nombre=input("cual es su nombre?: ")
print("hola", nombre, ", crea una contraseña")
contraseña= input("cree una contraseña: ")

ingresar= input("desea ingresar? si/no: ")

while True:
    if ingresar=="si":
        clave=input("ingrese su contraseña: ")
        if clave==contraseña:
            print("se ingreso correctamente")
            print ("bienvenido a calculadora basica")
            primer_num= int(input("ingrese primer numero: "))
            operacion= input ("desea sumar, restar, multiplicar, dividir: ")
            segundo_num= int(input("ingrese segundo numero: "))

            if operacion=="sumar":
                resolucion= primer_num + segundo_num
            elif operacion== "restar":
                resolucion= primer_num - segundo_num
            elif operacion== "multiplicar":
                resolucion= primer_num * segundo_num
            elif operacion== "dividir":
                resolucion= primer_num/segundo_num
            else: 
                print("ingrese operación válida")
            
            print("el resultado es:", resolucion)

        else:
            print ("la contraseña es incorrecta")

    else:
        print("cerrando sitio")
        break
    
    
