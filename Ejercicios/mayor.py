def mayorde3(vUno,vDos,vTres):
    vMayor=0
    if (vUno > vDos) :
            vMayor = vUno
    else:
            vMayor = vDos
    if (vDos < vTres) :
            vMayor = vTres
    return vMayor

print("3 elementos 1 8 7")
print("El valor mayor es  :",mayorde3(1,8,7))