from sympy.ntheory.factor_ import totient
import time
n = int(input())
inicio = time.time()
tot = totient(n)
fim = time.time()
print(tot)
print(fim-inicio)