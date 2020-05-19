def je_prastevilo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i < n / 2 + 1:
            if n % i != 0:
                i += 1
            else:
                return False
        return True

def prastevila_do_(n):
    seznam = []
    while n > 0:
        if je_prastevilo(n):
            seznam.append(n)
            n -= 1
        else:
            n -= 1
    return seznam

print(prastevila_do_(200))