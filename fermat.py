import random

# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

# You will need to implement this function and change the return value.
def mod_exp(x, y, N): 
	print("mod_exp")
	print("x", x)
	print("y", y)
	print("N", N)
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	if y % 2 == 0:
		return (z**2) % N
	else:
		return x * (z**2) % N
	
# You will need to implement this function and change the return value.   
def fprobability(k):
    return k

# You will need to implement this function and change the return value.   
def mprobability(k):
    return k

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N,k):
	print("fermat")
	print("N", N)
	print("k", k)
	for i in range(0, k):
		a = random.randint(2, N-1)
		print("a", a)
		if mod_exp(a, N-1, N) != 1:
			return 'composite'
	return 'prime'
# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
#  hi, inclusive.
def miller_rabin(N,k):
	print("miller_rabin")
	# find s and d
	d = N-1
	s = 0
	while d % 2 == 0:
		d = d // 2
		s += 1
	for i in range(0, k):
		a = random.randint(2, N-1)
		x = mod_exp(a, d, N)
		if x == 1 or x == N-1:
			continue
		for j in range(1, s):
			x = mod_exp(x, 2, N)
			if x == 1:
				return 'composite'
			elif x == N-1:
				break
			if x != N-1:
				return 'composite'
