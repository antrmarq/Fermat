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
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	if y % 2 == 0:
		return z*z % N
	else:
		return x*z*z % N	
# The time complexity of the mod_exp function is O(logn) because the function is called recursively logn times. The space complexity is O(logn) because the function is called recursively logn times.
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
	if N == 1:
		return 'composite'
	if N == 2:
		return 'prime'
	if(N == 3):
		return 'prime'
	if N % 2 == 0:
		return 'composite'
	for i in range(0, k):
		a = random.randint(2, N-1)
		if mod_exp(a, N-1, N) != 1:
			return 'composite'
	return 'prime'
#the time complexity of the fermat function is O(klogn) because the outer loop runs k times and the inner loop runs logn times. The space complexity is O(1) because the only variable that is stored is a, which is an integer.
#the issue with the accuracy of the fermat test is that it is not a strong test. It is possible for a composite number to pass the fermat test. For example, 561 is a composite number that passes the fermat test. This is because 561 is a Carmichael number, which is a composite number that passes the fermat test for all bases a coprime to n. The probability of a composite number passing the fermat test is 1/2^k, where k is the number of trials. This means that the probability of a composite number passing the fermat test decreases as k increases. However, the probability of a composite number passing the fermat test is never 0, so the fermat test is not a strong test.

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
	if N == 1:
		return 'composite'
	if N == 2:
		return 'prime'
	if(N == 3):
		return 'prime'
	if N % 2 == 0:
		return 'composite'
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
#the time complexity of the miller_rabin function is O(klog^2n) because the outer loop runs k times and the inner loop runs log^2n times. The space complexity is O(1) because the only variables that are stored are s and d, which are both integers.
# the miller-rabin test is a strong test because it is impossible for a composite number to pass the test. This is because the miller-rabin test is based on the fact that if n is a composite number, then there exists a nontrivial square root of 1 modulo n. The probability of a composite number passing the miller-rabin test is 4^(-k), where k is the number of trials. This means that the probability of a composite number passing the miller-rabin test decreases as k increases. However, the probability of a composite number passing the miller-rabin test is never 0, so the miller-rabin test is not a perfect test.