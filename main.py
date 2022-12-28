from get_random_dict import Get_Dict_сoeff as DICT   
from get_polinomial import Get_polynomial as POLYN
from get_polinomial_dict import Get_polinomial_dict as POLYNDICT
from get_sum_polynomial import Get_Sum_Polinoms as POLYNSUM

print()
coef_polinom_1 = DICT()
print()

with open ('polinomial1.txt','w') as polinom1:
    polinom1.write(POLYN(coef_polinom_1))
with open('polinomial1.txt','r') as polinom1:
    polinomial_1 = polinom1.read()
print(f'Первый многочлен:\n\n{polinomial_1}')
print()

dict_polinom_1 = POLYNDICT(polinomial_1)

coef_polinom_2 = DICT()
print()

with open ('polinomial2.txt','w') as polinom2:
    polinom2.write(POLYN(coef_polinom_2))
with open('polinomial2.txt','r') as polinom2:
    polinomial_2 = polinom2.read()
print(f'Второй многочлен:\n\n{polinomial_2}')

print(f'\n{"-"*100}')

dict_polinom_2 = POLYNDICT(polinomial_2)

sum_polinom_dic = POLYNSUM(dict_polinom_1, dict_polinom_2)
print()

sum_polinom = POLYN(sum_polinom_dic)

with open ('sum_polinomials.txt','w') as sum_polinom:
    sum_polinom.write(POLYN(sum_polinom_dic))
with open('sum_polinomials.txt','r') as sum_polinom:
    sum_polinom = sum_polinom.read()
print(f'Сумма многочленов:\n\n{sum_polinom}')
print()