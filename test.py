def je_prastevilo(n):
    i = 2
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        while i < n / 2 + 1:
            if n % i != 0:
                return False
            else:
                i += 1
        return True

def prastevila_do(n):
    seznam =[]
    i = 3
    while i <= n:
        if je_prastevilo(i):
            seznam.append(i)
            i += 1
        else:
            i += 1
    return [2] + seznam

print(prastevila_do(200))