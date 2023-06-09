from functools import lru_cache
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
@lru_cache()
def Fib(k):
    if (k<=1):
        return 1
    return Fib(k-1) + Fib(k-2)
k = int(input('Enter the desired fibonacci number: '))
print(f'Input: {k}')
print(f'Output: {Fib(k)}')