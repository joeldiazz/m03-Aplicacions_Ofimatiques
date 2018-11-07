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
