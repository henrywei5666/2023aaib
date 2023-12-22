s='00111'
n=len(s)
one=0 #想找出所有1
zero=0
for i in range(n):
  if s[i]=='1':one+=1 #如果是1,先全部加起來
  #現在就知道共有幾個one
#print('zero',zero,'one',one)
ans=0
for i in range(n-1): #要逐格修正,[吐出]一格，看他是多少就修正
  if s[i]=='0': #吐出0給左邊
    zero+=1   #左邊多1個0
  if s[i]=='1':  #吐出1給左邊
    one-=1    #右邊少1個1
  print('中間過程中','zero',zero,'one',one)
  ans=max(ans,zero+one)
print('答案找出來了',ans)