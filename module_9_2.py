first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) > 5]

second_result = [(i, s) for i in first_strings for s in second_strings if len(i)==len(s)]

list_strings = first_strings + second_strings

third_result = {x:  len(x) for x in list_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)