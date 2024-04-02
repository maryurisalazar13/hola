# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
# Maryuri Salazar 
# Alejandro Amaya
print("hola este programa te pide un numero y te muestra la tabla de multiuplicar de se numero")
numero = int(input("ingresa un numero: "))
print(f"tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
