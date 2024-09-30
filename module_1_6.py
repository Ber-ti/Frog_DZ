print('-------------------------------------------------------')#2

print('[2]:')
my_dict={'daniil': 2000, 'egor':2001, 'ivan': 1997}
print('   1)',my_dict)
print('   2)',my_dict.get('daniil'))
print('   3)',my_dict.get('vas'))
my_dict['daniil']=1999
my_dict.setdefault('masha',2058)
my_dict.setdefault('denis',2170)
print('   4)',my_dict)
print('   5)',my_dict.pop('daniil',1999))
print('   6)',my_dict)


print('-------------------------------------------------------')#3

print('[3]:')
my_set={'apple','banana','orange','pear','mango','lemon','banana','banana','lemon','lemon',11,23,11,56.33,2132,11}
print('   1)',my_set)
my_set.add(123)
my_set.add('ANTON')
my_set.add((1,2,3,4,5))
my_set.discard('banana')
print('   2)',my_set)

