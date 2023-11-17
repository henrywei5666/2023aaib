a=list(map(int,input().split()))
n=len(a)
for k in range(n):
	for i in range(n-1):
		if a[i]>a[i+1]:
			a[i],a[i+1]=a[i+1],a[i]
			
for i in range(n):
	print('',a[i],end='')
	if i % 10 == 9 and i != 99:
		print()
	