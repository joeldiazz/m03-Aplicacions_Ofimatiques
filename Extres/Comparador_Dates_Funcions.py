                             ##Python 3.6##
                    """Comparador d'anys amb funcions"""
    
    """Para utilizar este codigo debes poner: anyo(fecha_actual,fecha_cualquiera) 
    substituyendo fecha_actual y fecha_cualquiera por dos fechas."""
    
#Coding: utf-8
def anyo(actual,cualquiera):
    actual2=int(actual)
    cualquiera2=int(cualquiera)
    if((actual2 == 0 and cualquiera2 == 0)or(actual2 == 0)or(cualquiera2 ==0)):
        print("El año actual/cualquiera no puede ser 0")
    elif(actual2 == cualquiera2):
        print("Son el mismo año!")
    elif(actual2 < 0 and cualquiera2 < 0):
        if(actual2 > cualquiera2):
            print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2)+" años")
        else:
            print("Desde el año",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2)+" años")
    elif(actual2 < 0):
        if(actual2 > cualquiera2):
            print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2 - 1)+" años")
        else:
            print("Desde el",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2 - 1)+" años")
    elif(cualquiera2<0):
        if(actual2 > cualquiera2):
            print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2 -1)+" años")
        else:
            print("Desde el",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2 - 1)+" años")
    elif(actual2 > cualquiera2):
        print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2)+" años")
    else:
print("Desde el año",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2)+" años")
