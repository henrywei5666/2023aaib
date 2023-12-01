n=int(input())
a=[0,1]
for i in range(2,n+1):
	a.append(a[i-1]+a[i-2])
for i in range(n,-1,-1):
	print(f'f({i})={a[i]}')