first=input('number 1:')
second=input('number 2:')
third=input('number 3:')
#first=123
#second=124
#third=123
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)
