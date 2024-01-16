import random

# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

# You will need to implement this function and change the return value.
# psuedo code from class:
# if y == 0:
# z= mod_exp(x, floor(y/2), N)
# if y is even:
# return z^2 mod N
# else:
# return x*z^2 mod N
def mod_exp(x, y, N): 
	print("mod_exp")
	print("x", x)
	print("y", y)
	print("N", N)
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	if y % 2 == 0:
		return z*z % N
	else:
		return x*z*z % N	
	
# You will need to implement this function and change the return value.   
def fprobability(k):
    return 1/(2**k)

# You will need to implement this function and change the return value.   
def mprobability(k):
    return 4**(-k)

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

# psuedo code from wikipedia:
# Input #1: n > 2, an odd integer to be tested for primality
# Input #2: k, the number of rounds of testing to perform
# Output: “composite” if n is found to be composite, “probably prime” otherwise
# let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
# repeat k times:
#     a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
#     x ← ad mod n
#     repeat s times:
#         y ← x2 mod n
#         if y = 1 and x ≠ 1 and x ≠ n − 1 then # nontrivial square root of 1 modulo n
#             return “composite”
#         x ← y
#     if y ≠ 1 then
#         return “composite”
# return “probably prime”
def miller_rabin(N,k):
	print("miller_rabin")
	print("N", N)
	print("k", k)
	s = 0
	d = N - 1
	while d % 2 == 0:
		s += 1
		d = d // 2
	for i in range(0, k):
		a = random.randint(2, N-2)
		x = mod_exp(a, d, N)
		if x == 1 or x == N - 1:
			continue
		for j in range(0, s):
			y = mod_exp(x, 2, N)
			if y == 1 and x != 1 and x != N - 1:
				return 'composite'
			x = y
		if y != 1:
			return 'composite'
	return 'prime'
