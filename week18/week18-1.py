class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s) 
        a=s[:n//2] #前半段
        b=s[n//2:] #後半段
        motherA=0 #的母音有幾個   
        motherB=0 #的母音有幾個   
        for c in a: #在a裡面的每一個c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u': 
                motherA+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U' :
                motherA+=1
        for c in b:#在b裡面的每一個c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' :
                motherB+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U' :
                motherB+=1
        if motherA==motherB:return True
        else:return False