a=123456789012
b=98765432101

def gcd(a,b): #gcd最大公因數縮寫
  print(a,b)
  if a==0:return b
  if b==0:return a
  return gcd(b,a%b)
ans=gcd(a,b)
print(ans)