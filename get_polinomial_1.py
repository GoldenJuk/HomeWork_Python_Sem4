def Get_polynomial(my_dict:dict) -> str:
    polynomial = []
    
    for key, value in my_dict.items():
        if value != 0:
            polynomial.append(f'{value}*x**{key}')
    polynomial = ' ' + ' + '.join(polynomial) + ' = 0'                                               
    polynomial = polynomial.replace('+ -', '- ').replace('*x**0','')\
                           .replace('**1 ', ' ').replace(' 1*x', ' x')\
                           .replace(' -1*x', ' - x')
    return polynomial