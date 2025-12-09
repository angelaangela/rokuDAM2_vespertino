print("Escribe 20 numeros, los ordenare de menor a mayor, lo encontrare y te diré donde está situado")

#primero recojo los numeros y los meto en un array
contador = 1
posicion = 0
array_numeros = [0,0,0]
while(contador <= 5 ):
    numero = int(input(f"Introduce numero {contador}: "))
    array_numeros[posicion] = numero
    contador+=1
    posicion+1

print(f"El array queda asi: {array_numeros}")

 
    #print(f"El area sería: {area} y el perímetro: {perimetro}")


#ordenar de menor a mayor se puede ordenar de menor a mayor nuestro array


#buscar el numero dicotómicamente