#Lista de Busqueda
nombres=["Angel","Karla","Luis","Mateo","Maria","Luis","karla"]
print(f"Los nombres que se tienen son:{nombres}")
nombresBuscar=input("¿Que nombre deseas buscar?:")
encontrando=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombresBuscar:
        encontrando=True
        contador=contador+1
        print("Encontrado en la posicion:",i)
        i=i+1
    if encontrando==True:
        print("Nombre encontrado")
        print("Aparece",contador,"Veces")
    else:
        print("Nombre no encontrado")
    
