
print('Enter two integers: ')
a,b=map(int,input().split())
def gcd(a,b):
	if a==0:return b
	if b==0:return a
	return gcd(b,a%b)
ans=gcd(a,b)
print(f'The greatest common divisor of {a} and {b} is {ans}')
