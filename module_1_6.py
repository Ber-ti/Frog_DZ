print('-------------------------------------------------------')#2

print('[2]:')
my_dict={'daniil': 2000, 'egor':2001, 'ivan': 1997}
print(my_dict)
print(my_dict.get('daniil'))
print(my_dict.get('vas'))
my_dict['daniil']=1999
my_dict.setdefault('masha',2058)
my_dict.setdefault('denis',2170)
print(my_dict)
print(my_dict.pop('daniil',1999))
print(my_dict)


print('-------------------------------------------------------')#3

print('[3]:')
my_set={'apple','banana','orange','pear','mango','lemon','banana','banana','lemon','lemon',11,23,11,56.33,2132,11}
print(my_set)
my_set.add(123)
my_set.add('ANTON')
my_set.add((1,2,3,4,5))
my_set.discard('banana')
print(my_set)

