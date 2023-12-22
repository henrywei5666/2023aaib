a=input()
n=len(a)
bad=0

for i in range(n):
	if a[i]!=a[n-1-i]:
		bad+=1

if bad==0:print('YES',end='')
else:print('NO',end='')