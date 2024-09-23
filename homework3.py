from operator import truediv

my_strings=input('ввод:')
print('счетчик символов(str): ',len(my_strings))
print('[1]:',my_strings.upper())
print('[2]:',my_strings.lower())
print('[3]:the initial character', my_strings[0])
print('[4]:the last character', my_strings[-1])
ass=my_strings.isalnum()
print(ass)