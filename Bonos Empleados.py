Nombre=input("Nombre del empleado")
Pago_hora=float(input("pago por hora: $"))
Horas_mes=float(input("horas trabajadas al mes"))
Sueldo=Pago_hora*Horas_mes
Bono=0
if Sueldo>=100 and Sueldo<=300:
    Bono=500
    print('f"tu sueldo es"{500+500}')
elif Sueldo>300 and Sueldo<=1500:
    Bono=1700
elif Sueldo>1500 and Sueldo<=3000:
    Bono=3500
elif Sueldo>3000 and Sueldo<=8000:
    Bono=8500
elif Sueldo>8000:
    Bono=10000
else:print("no valido")

