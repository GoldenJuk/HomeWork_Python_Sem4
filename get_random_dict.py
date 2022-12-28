from random import randint as RN

def Get_Dict_сoeff() -> dict:
    k = int(input('Введите наивысшую степень: '))
    dict_coef = {}

    for i in range(k, -1, -1):
        dict_coef[i] = (RN(-100,100))
        if dict_coef[k] == 0:
            dict_coef[k] = (RN(-100,100))
            
    return dict_coef
