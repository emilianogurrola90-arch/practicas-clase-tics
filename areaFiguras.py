#Programa para calcular areas
#Areas cuadrado; lado x lado 
lado=float(input("ingresa el lado"))
areaCuadrado=lado*lado
print("El area es ", areaCuadrado)
print(f'El area es {areaCuadrado}')
altura=float(input("ingresa la altura"))
base=float(input("ingresa la base"))
areaTriangulo=(base*altura)/2
print("El area es ", areaTriangulo)
print(f'El area es {areaTriangulo}')
baseMayor=float(input("ingresa la base mayor"))
baseMenor=float(input("ingresa la base menor"))
altura=float(input("ingresa la altura"))
areaTrapecio=(baseMayor+baseMenor)*altura/2
print("El area es ", areaTrapecio)
print(f'El area es {areaTrapecio}')
Pi=float(input("ingresa el valor Pi"))
radio=float(input("ingresa la radio"))
areaCirculo=Pi*radio*radio
print("El area es", areaCirculo)
print(f'El area es {areaCirculo}')
perimetro=float(input("ingresa el perimetro"))
apotema=float(input("ingresa la apotema"))
areaPentagono=perimetro*apotema/2
print("El area es", areaPentagono)
print(f'El area es {areaPentagono}')


