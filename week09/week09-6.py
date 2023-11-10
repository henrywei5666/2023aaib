a=input().split()
n=100
for i in range(n):
	a[int(i)]

for k in range(n):
	for i in range(1,n):
		if a[i]<a[i-1]:
			a[i],a[i-1]=a[i-1],a[i]
for i in range(n):
	print(a[i])