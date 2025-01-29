def is_prime(func):
    def wrappper(*nambers):
        simpl = func(*nambers)
        x = True
        for i in range(2, simpl - 1):
            if simpl % i == 0:
                x = False
                break
        if x:
            print('Простое')
        else:
            print('Составное')
        return simpl

    return wrappper


@is_prime
def sum_three(*nambers):
    return sum(nambers)


result = sum_three(2, 3, 6)

print(result)
