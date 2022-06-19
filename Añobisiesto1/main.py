Año = int(input("Introduzca año"))

if Año % 4 == 0:
    if Año % 100 == 0:
        if Año % 400 == 0:
            print("Es un año bisiesto")
        else:
            print("Es año común")
    else:
        print("Es un año bisiesto")
else:
    print("Es un año común")