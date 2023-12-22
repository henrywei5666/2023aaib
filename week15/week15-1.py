class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        for left in range(len(s)-1):#-1留給右邊
        #0...left left+1...len(s)-1 左幾個零 右幾個一
            now=0
            for i in range(len(s)):
                if i<=left and s[i]=='0':now+=1
                if i>left and s[i]=='1':now+=1
            if now>ans:ans=now
        return ans

