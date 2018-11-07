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
                    """Comparador d'anys amb negatius"""
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
            if(res_act <= 0):
                neg_act= (res_act + 1)
                if(neg_act == 0):
                    print("Para llegar al año ",Futuro," falta 1 año")
                else:
                    print("Para llegar al año ",Futuro," faltan ",neg_act," años")
        else:
            if(Actual > Futuro):
                res_fut=(Actual - Futuro)
                if(Actual <= 0 or Futuro <=0):
                    neg_fut= (res_fut + 1)
                    if(neg_fut == 0):
                        print("Desde el año ",Futuro," ha pasado 1 año")
                    else:
                        print("Desde el año ",Futuro," han pasado ",neg_fut," años")
                else:
                    print("Desde el ",Futuro," han pasado ",res_fut," años")
            else:
                if(Actual == Futuro):
                    print("Son el mismo año!")
