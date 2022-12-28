def Get_polinomial_dict(polinomial:str) -> dict:

    polinomial = polinomial.replace(' + ',' ').replace(' - ',' -')\
                           .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
                           .replace('*x ','*x**1 ').split()[:-2]
    polinomial_dict ={}

    for item in polinomial:
        i = item.split('*x**')
        if len(i) > 1:
            polinomial_dict[int(i[1])] = int(i[0])
        elif len(i) == 1:
            polinomial_dict[0] = int(i[0])

    return polinomial_dict
