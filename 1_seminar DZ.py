########## Урок 1. Расчет вероятности случайных событий

########## Условие:

########## 1.Из колоды в 52 карты извлекаются случайным образом 4 карты. 
########## a) Найти вероятность того, что все карты – крести. 
from math import factorial
deck = 52  # всего карт
suit = 13  # количество карт по масти (подмножество крести)
other = 52-suit  # Оставшиеся масти карт
i = 4  # количество карт необходимо взять

m = factorial(suit)/(factorial(i)*factorial(suit-i))
n = factorial(deck)/(factorial(i)*factorial(deck-i))

Probability=m/n
print (Probability)#0.0026410564225690276
########## Что составляет 0,264%

########## б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# К сожалению запутался на семинаре как это должно было выглядеть.




######### 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
######### Код содержит три цифры, которые нужно нажать одновременно. 
######### Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
k=10        #Количество кнопок в замке
x=3         # Количество кнопок в коде
combination_code = factorial(x) #Количество комбинаций кода
total_combinations = factorial(k) #Всего комбинаций в замке

Probability_code=combination_code/total_combinations

print(Probability_code)# 1.6534391534391535e-06
######### Что составляет 0,0001653439%

########## 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того,
########## что все извлеченные детали окрашены?
d=15 #Количество деталей
o=9 # Окрашенных
y=3 # извлеченные

all_outcomes=factorial(d)/(factorial(y)*factorial(d-y))
favorable_outcomes=factorial(o)/(factorial(y) * factorial(o-y))

probability_outcomes=favorable_outcomes/all_outcomes
print(probability_outcomes)#0.18461538461538463
#########Что составляет 18,4%

########## 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
f=100 #Всего билетов
s=2   #Выигрышных 
u= 98 #Не выигрышные билеты
e=0 #невыигрышные билеты
Total_combinations=factorial(f)/(factorial(s)*factorial(f-s))
Winning_combinations=(factorial(s)/(factorial(s)*factorial(s-s)))*((factorial(u)/(factorial(e)*factorial(u-e))))



Probability_of_winning=Winning_combinations/Total_combinations
print(Probability_of_winning) #0.00020202020202020202
######Что составляет 0,02%


