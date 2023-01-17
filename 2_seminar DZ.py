##    Задача №1
##  Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
##  Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
## Решение:
## Применяем формулу Бернулли, где:
from math import factorial

hits_on_target = 85  # число наступления события (дискретная величина из отрезка [0, 𝒏])
number_of_trials = 100  # число испытаний
shot_probability = 0.8  # вероятность наступления события 𝑨 в  независимых испытаниях,
opposite_probability = 0.2  # 𝟏 – 𝒑. Противоположная вероятность

i = factorial(number_of_trials)/(factorial(hits_on_target)
                                 * factorial(number_of_trials - hits_on_target))
print(i)  # 2.5333847134998864e+17

x = i * (shot_probability)**(hits_on_target) * (opposite_probability)**(number_of_trials -
                                                                        hits_on_target)  # Вероятность того, что стрелок попадет в мишень, выстрелив один раз
print("{:.10f}".format(x))  # 0.0480617937
# Ответ: 4.8061 %


# ##   Задача №2
# ## Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# ## В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# ## Какова вероятность, что ни одна из них не перегорит в первый день? 
# ## РЕшаем по формуле Распределение Пуассона
bulb_burnout = 0.0004
number_of_bulbs = 5000
will_not_burn_out = 0
euler_number = 2.718281828459045235360287471352

lmd = number_of_bulbs * bulb_burnout  # 2 = лямбда
print(lmd)

p1 = (lmd ** (will_not_burn_out)/factorial(will_not_burn_out)) * \
    euler_number**(-lmd)
        
print("{:.10f}".format(p1)) ## 0.1353352832
##  Ответ: 13.4334%



# ##  Задача №2а
# ## Какова вероятность, что перегорят ровно две?
number_of_burnt_out = 2
p2 = (lmd ** (number_of_burnt_out)/factorial(number_of_burnt_out)) * \
    euler_number**(-lmd)

print("{:.10f}".format(p2)) ##  0.2706705665
##  Ответ: 27.06705665 %




# ##  Задача №3
# ## Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?


tossed_up=144
possible_outcome = 0.5
opposite_probability = 1-0.5
number_of_occurrences = 70


w= factorial(tossed_up)/(factorial(number_of_occurrences)
                                 * factorial(tossed_up - number_of_occurrences))
drop_probability = w * (possible_outcome**number_of_occurrences) * (opposite_probability**(tossed_up-number_of_occurrences))
print("{:.10f}".format(drop_probability)) ## 0.06281178035144776
##Ответ: 6.281%



# ##  Задача №4
# ## В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, 
# ## из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча.
# # ## Какова вероятность того,что все мячи белые? 
box_one = 10
white_balls_in_the_first_box = 7
Second_box = 11
white_balls_in_the_second_box = 9
took_out_the_ball = 2

P1= ((white_balls_in_the_first_box/box_one)*(6/9))*((white_balls_in_the_second_box/Second_box)*(8/10))

print(P1) ##0.3054545454545455
## Ответ: 


# ##  Задача №4а
# ## Какова вероятность того, что ровно два мяча белые? 
# ##Получается 6 комбинаций из шаров
# ## 1. белый белый - черный черный
# ## 2. черный черный - белый белый
# ## 3. белый черный - черный белый
# ## 4. белый черный -белый черный
# ## 5. черный белый - черный белый
# ## 6. черный белый - белый черный

T = (7/10)*(6/9)*(2/11)*(1/10) + (7/10)*(3/9)*(9/11)*(2/10) + (7/10)*(3/9)*(2/11)*(9/10) + (3/10)*(7/9)*(9/11)*(2/10) + (3/10)*(7/9)*(2/11)*(9/10) + (3/10)*(2/9)*(9/11)*(8/10)
print(T) ## 0.20484848484848484
## Ответ: 20.484848 %


# ##  Задача №4б
# ## Какова вероятность того, что хотя бы один мяч белый?

L = 1-(3/10*2/9*2/11*1/10)
print(L) ## 0.9987878787878788
## Ответ: 99.87%

