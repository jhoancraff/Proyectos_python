def conversor(tipo_moneda, valor_dolar):
    moneda = input("¿Cuantos " + tipo_moneda + " tienes?")
    moneda = float(moneda)
    dolares = moneda / valor_dolar
    dolares = str(dolares)
    print("tienes $ " + dolares + " dolares" )

menu = """
    Hola bienvenido al convertidor de monedas

    1- Bolivares
    2- Pesos colombianos
    3- Soles
    4- Pesos mexicanos
    5- Pesos chilenos

    Elige una opcion:

"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Bolivares", 5.20)
elif opcion == 2:
    conversor("Pesos colombianos", 4200)
elif opcion == 3:
    conversor("Soles", 4)
elif opcion == 4:
    conversor("Pesos mexicanos", 19.90)
elif opcion == 5:
    conversor("Pesos clilenos", 837)
else:
    print("Opcion incorrecta, eliga una de las 5 opciones")                    

