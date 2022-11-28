def EstaEnlista(valor, lista):
    if valor in lista:
        return True
    else:
        return False

def EstaEnRango(valor, minimo, maximo):
    if valor >= minimo and valor <= maximo :
        return True
    else:
        return False
    
# funcion 1ª comprobación: print(EstaEnlista(9,[1,2,3,4,5,6]))
# funcion 2ª comprobación: print(EstaEnRango(1, 1, 19))