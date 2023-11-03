a=[3,0,1,8,7,2,5,4,6,9]
print(a)
for i in range(1,len(a)):
  if a[i]<a[i-1]: #比大小
    a[i],a[i-1]=a[i-1],a[i]
print(a) #排一輪後印出