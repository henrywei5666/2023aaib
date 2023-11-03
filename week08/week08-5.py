a=[9,8,7,6,5,4,3,2,1,0]
print(a)
for k in range(len(a)):
  for i in range(1,len(a)):
    if a[i]<a[i-1]: #比大小
      a[i],a[i-1]=a[i-1],a[i]
  print(a) #排一輪後印出