def sumarpares(vLista):
    vSuma=0
    i=0
    while i < len(vLista):
        if vLista[i] % 2 == 0:
            vSuma = vSuma + vLista[i]
            i += 1
        else:
            i += 1
    return vSuma

vValores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # lista de 10
print("10 elementos sumar solo pares")
print("sumar de pares :",sumarpares(vValores))