def password(number):
    duck = []#Список: "Для чего я создан?" Я: "Для пробелов!" Список: "б*#@"
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                duck.append( str(i) + str(j))
    return duck
while 1 > 0:
    print('Чтобы выйти из цикла, введите «0».')
    input_=int(input('Введите число: '))
    print(*password(input_))
    if input_ == 0:
        print('Цикл завершен')
        break
    else:
        continue

#Все пароли для чисел от 3 до 20 (для сверки):

# 3 - 12
#
# 4 - 13
#
# 5 - 1423
#
# 6 - 121524
#
# 7 - 162534
#
# 8 - 13172635
#
# 9 - 1218273645
#
# 10 - 141923283746
#
# 11 - 11029384756
#
# 12 - 12131511124210394857
#
# 13 - 112211310495867
#
# 14 - 1611325212343114105968
#
# 15 - 1214114232133124115106978
#
# 16 - 1317115262143531341251161079
#
# 17 - 11621531441351261171089
#
# 18 - 12151811724272163631545414513612711810
#
# 19 - 118217316415514613712811910
#
# 20 - 13141911923282183731746416515614713812911