# Paso 1: Definir el tipo de cambio

tc_usd_mxn=23.70
tc_eur_mxn=23.70

# Paso 2: Solicitar al usuario el Tipo de conversión (euro a peso mex o dolar a peso mex)

tipo_de_conversión= input("Ingrese la moneda de origen para la conversión (usd/eur): ")

# Paso 3: Solicitar el monto a convertir
monto_a_convertir=float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el TC correspondiente
# Paso 5: Mostrar al usuario la conversión ya realizada

if tipo_de_conversión.upper() == "EUR":
    conversion= monto_a_convertir * tc_eur_mxn
    print("El resultado de la conversión de EUR a MXN es: ",conversion)
elif tipo_de_conversión.upper() == "USD":
    conversion= monto_a_convertir * tc_usd_mxn
    print("El resultado de la conversión de EUR a MXN es: ",conversion)
else:
    print("Tipo de conversión no válido")
