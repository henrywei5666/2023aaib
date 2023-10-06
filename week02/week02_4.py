a=int(input())
if a>=90: ans='A'
if 80<=a<90: ans='B'
if 70<=a<80: ans='C'
if 60<=a<70: ans='D'
if a<60: ans='F'
print(ans,end='')