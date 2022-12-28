def Get_Sum_Polinoms(first_dict:dict, second_dict:dict):
    sum_dict = {}
    sum_dict.update(first_dict)
    sum_dict.update(second_dict)
    sum_dict = dict(sorted(sum_dict.items(), reverse = True))

    for key in sum_dict:
        sum_dict[key] = first_dict.get(key, 0) + second_dict.get(key, 0)
        
    return sum_dict  