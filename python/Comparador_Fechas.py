                        ##Python 3.6##
             """Comparador d'anys sense negatius"""
#Coding: utf-8
Actual= int(input("Indique el año actual: "))
Futuro= int(input("Pon un año cualquiera: "))
if(Actual == 0):
    print("El año actual no puede ser 0")
else:
    if(Futuro == 0):
        print("El año cualquiera no puede ser 0")
    else:
        if(Actual < Futuro):
            res_act=(Futuro - Actual)
            print("Para llegar al año ",Futuro," faltan ",res_act," años")
        else:
            if(Actual > Futuro):
                res_fut=(Actual - Futuro)
                print("Desde el ",Futuro," han pasado ",res_fut," años")
            else:
                if(Actual == Futuro):
                    print("Son el mismo año!")
                    
**************************************************************************************************
                             ##Python 3.6##
                    """Comparador d'anys amb negatius sense errors"""
#Coding: utf-8
Actual= int(input("Indique el año actual: "))
Futuro= int(input("Pon un año cualquiera: "))
if(Actual == 0 and Futuro == 0):
    print("El año actual y el año cualquiera no pueden ser 0, saludos.")
else:
    if(Actual == 0):
        print("El año actual no puede ser 0")
    else:
        if(Futuro == 0):
            print("El año cualquiera no puede ser 0")
        else:
            if(Actual < Futuro):
                res_act=(Futuro - Actual)
                if(res_act <= 0):
                    if(Actual < 0 and Future < 0):
                        print("Para llegar al año ",Futuro," faltan ",res_act," años")
                    else:
                        neg_act= (res_act + 1)
                        if(neg_act == 0):
                            print("Para llegar al año ",Futuro," falta 1 año")
                else:
                    print("Para llegar al año ",Futuro," faltan ",res_act," años")
            else:
                if(Actual > Futuro):
                    res_fut=(Actual - Futuro)
                    if(Actual <= 0 or Futuro <=0):
                        neg_fut= (res_fut - 1)
                        if(neg_fut == 0):
                            print("Desde el año ",Futuro," ha pasado 1 año")
                        else:
                            if(Actual <= 0 and Futuro <= 0):
                                print("Desde el ",Futuro," han pasado ",res_fut," años")
                            else:
                                print("Desde el año ",Futuro," han pasado ",neg_fut," años")
                    else:
                        print("Desde el ",Futuro," han pasado ",res_fut," años")
                else:
                    if(Actual == Futuro):
                        print("Son el mismo año!")
                        
**************************************************************************************************
                             ##Python 3.6##
                    """Comparador d'anys amb funcions"""
    
    ###Para utilizar este codigo debes poner [anyo(fecha_actual,fecha_cualquiera)] substituyendo fecha_actual y fecha_cualquiera por dos fechas.##
    
#Coding: utf-8
def anyo(actual,cualquiera):
    "Uso: tiempo(año actual, año cualquiera)"
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
    elif(actual2<0):
        if(actual2 > cualquiera2):
            print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2 - 1)+" años")
        else:
            print("Desde el",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2 - 1)+" años")
    elif(cualquiera2<0):
        if(actual2 > cualquiera2):
            print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2)+" años")
        else:
            print("Desde el",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2 - 1)+" años")
    elif(actual2 > cualquiera2):
        print("Para llegar al año",cualquiera,"al",actual2,"faltan "+str(actual2 - cualquiera2)+" años")
    else:
        print("Desde el año",cualquiera,"al",actual2,"han pasado "+str(cualquiera2 - actual2)+" años")
    
