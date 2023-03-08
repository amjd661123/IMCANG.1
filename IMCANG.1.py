### Declaración de Variables y Datos

nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Ingresa estatura en metros: "))
masa = float(input("Ingresa masa en Kilogramos: "))

### Validación de Datos para edad

if edad<0:
     print('No es posible tener edad negativa por favor introduce un valor real')

elif edad<18:
     print(str(nombre)+ " es menor de Edad")

else:
    print(str(nombre)+ ' es mayor de edad')


### Validación de la estatura

if estatura<0:
     print("La estatura no puede ser un numero negativo o inferior a a 0 por favor introduce un valor valido.")

else:
     print(str(nombre) + " mide " + str(estatura))

 ### Validación de la estatura

if masa<0:
     print("La masa no puede ser un numero negativo o inferior a a 0 por favor introduce un valor valido.")

else:
    print(str(nombre) + " tiene una masa corporal de  " + str(masa))   




### Calculo del IMC

IMC = float(masa/estatura**2 )
print(f'El índice de masa corportal de {nombre} es de {IMC: .2f}')

#Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
elif IMC >= 40.00:
        print ("obesidad morbida")
