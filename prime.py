def prime(n):
	numbers = list(range(n+1))
	if isinstance(n,int):
		if n==0:
			return []
		if n == 2:
			return [2]
		for num in range(n+1):
			if not n%2 == 0 and n > 2:
				for i in range(3,int(math.sqrt(num)) + 1, 2):
					if num%i == 0:
						numbers.remove(num)
		return numbers
	else:
		raise ValueError

print (prime(10))