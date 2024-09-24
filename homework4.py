immutable_var=([258,2654],True,'sas')
print('[2]:',immutable_var)

immutable_var=([258,2654],True,'sas')
immutable_var[0][0]=546
print('[3]:',immutable_var)
print('[3.1]:')
#Кортежи (тип tuple) — это неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.

#Можно поменять список в кортеже, но кортеж в...я хз
immutable_var=[(9,8),3,4]
#immutable_var[0][0]=10
print('   ',immutable_var[0][0])
#Оказывается нельзя:D

#Вы спросите, а как взаимодействовать с кортежем?

#1)Добавление инфы в кортеж
immutable_var=([258,2654],True,'sas')+(2,'gacha')
print('   ',immutable_var)
#2)Дублирование
immutable_var=([258,2654],True,'sas')*2
print('   ',immutable_var)
#3)Извлечение инфы для использования
immutable_var=([258,2654],True,'sas')
igef=(immutable_var[0][0])+2
print('   ',type(immutable_var[0]))
print('   ',igef)

mutable_list=[1,23,True,'sas']
mutable_list[2]=False
print('[4]:',mutable_list)