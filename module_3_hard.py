def calculate_structure_sum(n):
    sum = 0
    if isinstance(n, dict) == True:
        for k, v in n.items():
            sum += calculate_structure_sum(k)
            sum += calculate_structure_sum(v)
    elif isinstance(n, list) == True:
        for i in n:
            sum += calculate_structure_sum(i)
    elif isinstance(n, tuple) == True:
        for a in n:
            sum += calculate_structure_sum(a)
    elif isinstance(n, set) == True:
        for f in n:
            sum += calculate_structure_sum(f)
    elif isinstance(n, float) == True:
        sum += n
    elif isinstance(n, int) == True:
        sum += n
    elif isinstance(n, str) == True:
        sum += len(n)
    return sum



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

