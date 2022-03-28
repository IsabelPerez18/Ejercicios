vListaTupla = ('Lista')  # declaramos la tupla
vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26,49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]  # delaramos la lista
print('Eliminar de la lista, todas las ocurrencias del entero 10')
print(vListaTupla+' con vacunados de 10 años -----------------')
print(vEdades) # imprimimos la lista
x = 0          #  declaramos una variable de control para el ciclo
while x < len(vEdades):     #ciclo haga mientras la condicion de la variable de control sea menor que el tamaño de la lista
    if vEdades[x] == 10:    #condicional si la lista en la posicion de la varaible de control es igual a 10 entonces
        vEdades.pop(x)      #se borra el elemento de la lista
    x += 1                  #Incremento la variable de control luego de verificar los valores de la lista
print(vListaTupla+' sin los vacunados de 10 años ----------------')
print(vEdades)      #imprimimos la lista para verificar que se borraron los valores 
