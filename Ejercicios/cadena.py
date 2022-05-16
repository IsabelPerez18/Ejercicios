def cadena(vCadena,vCantidad):
    vMitad = int(len(vCadena) / 2)
    vCentro = int(vCantidad / 2)
    vAjuste = vCentro - vMitad
    vSalida = vCadena.center(vCantidad," ")
    return vSalida,str(vAjuste)

print("cadena a centrar")
print("cadena debe ser:",cadena("Gato",20))