a=[1,3,5,7,9,11,13,15,17]
for i in range(1,len(a)):
  print('現在檢查',a[i],a[i-1])
  if a[i]-a[i-1] != a[1]-a[0]:#某兩項相減若不為2則失敗
    print('失敗',a[i],a[i-1])

print('程式檢查結束')