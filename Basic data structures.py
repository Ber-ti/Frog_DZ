students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_list=sorted(list(students))

print(' '
      'v1'
      ' ')#-----------------------------------------------------------v1

mean_grades=[round(sum(grades[0])/len(grades[0]),2),
             round(sum(grades[1])/len(grades[1]),2),
             round(sum(grades[2])/len(grades[2]),2),
             round(sum(grades[3])/len(grades[3]),2),
             round(sum(grades[4])/len(grades[4]),2)]
dict1=dict(zip(students_list, mean_grades))
print(dict1)

print(' '
      'v2'
      ' ')#-----------------------------------------------------------v2

ass=dict(zip(students_list, grades))
mean_grades2=[ round(sum(ass['Aaron'])/len(ass['Aaron']),2),#что?
               round(sum(ass['Bilbo'])/len(ass['Bilbo']),2),
               round(sum(ass['Johnny'])/len(ass['Johnny']),2),#почему?
               round(sum(ass['Khendrik'])/len(ass['Khendrik']),2),
               round(sum(ass['Steve'])/len(ass['Steve']),2)]
ass2=dict(zip(students_list, mean_grades2))
print(ass2)

print(' '
      'что-то:D'
      ' ')

x=input('имя: ')
print('оценки:',ass.get(x))
print('ср-я оценка:',ass2.get(x))
sas=ass.get(x)
sad=sas.append(int(input('добавить оценку? ')))

print(ass)
print(round(sum(ass['Steve'])/len(ass['Steve']),2))
print(' '
      'v3'
      ' ')#-----------------------------------------------------------v3
# #должна ли быть четкая последовательность?
#ass4=dict(zip(students_list, grades))
#mean_grades3=[ round(sum(ass['Johnny'])/len(ass['Johnny']),2),#почему?
 #              round(sum(ass['Bilbo'])/len(ass['Bilbo']),2),
  #             round(sum(ass['Aaron'])/len(ass['Aaron']),2),#что?
   #            round(sum(ass['Khendrik'])/len(ass['Khendrik']),2),
    #           round(sum(ass['Steve'])/len(ass['Steve']),2)]
#ass3=dict(zip(students_list, mean_grades3))
#print(ass3)
#ass[x]=input('добавить оценку? ')#нет
#sws={'esw':[[{'ec':12}],[(1,2.3)],[12,44,678]]}
#print(sws.get('esw'.g,'ec'))