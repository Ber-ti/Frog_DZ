def all_variants(text):
    for i in text:
        yield i
    f=0
    for i in text[1:]:
        if i == text[-1]:
            yield text[0 + f] + i
            yield text
        else:
            yield text[0+f] + i
            f = f + 1

a = all_variants("abc")
for i in a:
    print(i)

#Опишите логику работы внутри функции all_variants.
# ¯\(°_o)/¯ специальная функция, которую мы создаём, и которая возвращает итератор