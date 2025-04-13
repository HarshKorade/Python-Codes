class Solution:
    def remove_duplicate(self, arr):
        l = []
        s = set()
        for i in arr:
            if i not in s:
                s.add(i)
                l.append(i)
        return l
a = Solution()
arr = [1,1,2,2,2,2,3]
print(a.remove_duplicate(arr))
