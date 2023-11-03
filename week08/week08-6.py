class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        # for k in range(len(arr)):
        #     for i in range(1,len(arr)):
        #         if arr[i]<arr[i-1]:
        #             arr[i],arr[i-1]=arr[i-1],arr[i]
        arr.sort()


        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True    