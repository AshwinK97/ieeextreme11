# return the nth fibbonaci number
def fib(n):
    a, b = 0, 1
    for i in range(0,n):
        b = a + b
        a = b - a
    return b

questions = int(input())
for q in range(0, questions):
    print fib(int(input()))

