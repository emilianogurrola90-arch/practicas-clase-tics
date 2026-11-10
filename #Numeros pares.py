#Numeros pares 
Numeros=[]
NumPares=[]
i=0
while i<10:
    Num=int(input("ingresa un numero:"))
    Numeros.apped(Num)
    i=i+1
    print("Numeros pares:")
    for Num in Numeros:
        if Num %2==0:
            print(Num)
            NumPares.append(Num)
print("Lista Numpares:", NumPares)

