colls = 0

def count_calls():
     global colls
     colls+=1

def string_info(n):
    count_calls()
    s = len(n)
    a = n.upper()
    f = []
    f.append(s)
    f.append(a)
    f.append(n)

    return tuple(f)


def is_contains(n, s):
    count_calls()
    d = []
    for i in s:
        d.append(i.upper())
    if n.upper() in d:
        return True
    else:
        return False
    print()





print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(colls)
