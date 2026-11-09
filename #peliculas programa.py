#peliculas programa
#Ponerle nombre a mi lista
Peliculas=[]
#Preguntar cuantas pelis
CantidadPelis=int(input("cuantas peliculas vas a agregar"))
#Valor inicial para el while
i=0
#Mientras i sea menor a cantidad ejecutada
while i<CantidadPelis:
    #Preguntar peliculas
    Peli=input("ingresa peli: ")
    #Agrega peliculas a la lista
    Peliculas.append(Peli)
    #Muestra la lista
    print(Peliculas)
    i=i+1
    #Buscar una pelicula en la lista
    #Preguntar la peli que busca
    PeliBuscar=input("que peli buscas")
    if PeliBuscar in Peliculas:
        print("si esta")
    else:
        print("No esta pero dejame la agrego")
        Peliculas.append(PeliBuscar)
        print(Peliculas)

