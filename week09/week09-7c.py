a=input().split()
n=int(a[0])
ans=0
for i in range(1,n+1):
	ans+=int(a[i])
print(ans)