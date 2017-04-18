def prime(n):
	prime_numbers = []
	if isinstance(n,int) and n > 0:
		if n==0:
			print([])
		else:
			for num in range(0, n+1):
				if num > 1:
					for i in range(2,num):
						if num%i == 0:
							break
							'''numd = numbers.remove(num)'''
					else:
						print(num)
	else:
		raise TypeError('Argument must be positive integer')

prime(10)
prime(-7)
prime('10')