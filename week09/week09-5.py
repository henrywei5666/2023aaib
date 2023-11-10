class Solution:
    def average(self, salary: List[int]) -> float:
        #算平均的方法:(加起來)再除(數量)
        n=len(salary)
        ans=(sum(salary)-max(salary)-min(salary))/(n-2)
        return ans