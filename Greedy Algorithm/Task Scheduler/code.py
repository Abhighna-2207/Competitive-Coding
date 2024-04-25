class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks)
        max_freq=max(d.values())
        no_max_freq=sum(1 for count in d.values() if count == max_freq)
        res=(max_freq-1)*(n+1)+no_max_freq
        return max(res,len(tasks))

        
