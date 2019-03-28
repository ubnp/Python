'''
变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
普通函数调用直接返回结果,generator函数的“调用”实际返回一个generator对象，如：<generator object fib at 0x1022ef948>
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(eval(input("Enter a max number：")))
f
