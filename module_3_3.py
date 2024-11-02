calls = 0

def count_calls():
     global calls
     calls+=1


def print_params(a = 1, b = 'строка', c = True):
    count_calls()
    print(f'{calls}:', a, b, c)


print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(123, 1234, )
print_params('wad', 345, False)
print_params()


values_list = [12, 'sas', True]
values_dict = {'a': 'fas', 'b': 245.49, 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)