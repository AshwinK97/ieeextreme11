def fib_to(n):
	fibs = [1, 1]
	for i in range(2, n+1):
		fibs.append((fibs[-1] + fibs[-2]) % 10)
		fibs.pop(0)
	return fibs[-1] % 10

questions = int(input())
for q in range(0, questions):
   print fib_to(long(input()))