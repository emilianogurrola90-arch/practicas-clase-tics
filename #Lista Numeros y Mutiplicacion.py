#Lista Numeros y Mutiplicacion
Numeros=[]
Resultados=[]
i=0
while i<5:
    num=int(input("Ingresa un numero:"))
    Numeros.append(num)
    i=i+1
    multiplicador=int(input("¿Por cuanto deseas multiplicar?:"))
    for num in Numeros:
        resultado=num*multiplicador
        Resultados.append(Resultados)
    print("Numeros originales:", Numeros)
    print("Resultados:", Resultados)
    Buscar=int(input("¿Que numero deseas buscar en resultados?:"))
    if Buscar in Resultados:
        print("Si aparece en resultados")
    else:
        print("No aparece en resultados")