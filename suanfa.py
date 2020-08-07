class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        print(a)
        s = len(a) % 2
        if s:
            return a[len(a)//2]
        else:
            z = len(a) // 2
            return (a[z] + a[z-1]) / 2


class LRUCache:

    def __init__(self, capacity: int):
        self.list = []
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if self.dict.get(key):
            a = self.list.pop(self.list.index(key))
            self.list.append(a)
            return self.dict.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if self.dict.get(key) or len(self.dict) < self.capacity:
            self.dict[key] = value
            self.list.append(key)
        else:
            del self.dict[self.list[0]]
            self.list.pop(0)
            self.dict[key] = value

class Solution1():
    def subarraysDivByK(self,A,k):
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            print(modulus,same,ans)
            record[modulus] = same + 1
        print(record)
        return ans


class Solution3:
    def rob(self, nums):
        dp = [0 for _ in range(len(nums) + 2)]  # dp数组的每一个位置存到到当前位置可以得到的最大值
        for i in range(len(nums)):
            dp[i + 2] = max(nums[i], dp[i + 1], nums[i] + dp[i])
        return dp[-1]






if __name__ == '__main__':
    # s = Solution()
    # a = [1,3]
    # b = [2]
    # # a = s.findMedianSortedArrays(a,b)
    # # print(a)
    # f = a.pop(1)
    # print(f)
    # cache = LRUCache(2)
    # a = cache.put(1, 1)
    # b = cache.put(2, 2)
    # c = cache.get(1) # 返回 1
    # d = cache.put(3, 3)# 该操作会使得关键字
    # e = cache.get(2) # 返回 - 1(未找到)
    # f = cache.put(4, 4) # 该操作会使得关键字
    # g = cache.get(1) # 返回 - 1(未找到)
    # h = cache.get(3) # 返回 3
    # v = cache.get(4) # 返回 4
    # import collections
    # collections.Counter()
    # a = {1:3}
    # v = Solution1()
    # A = [4,5,0,-2,-3,1]
    # p = 5
    # v.subarraysDivByK(A,p)
    # a = "[[1],[0] *2] *3"
    # print(eval(a))
    # s = Solution3()
    # r = s.rob([2,1,1,2])
    # print(r)
    import os,sys
    # print(os.path.join(os.path.dirname(__file__), 'ooo.py'))
    print({1:2})
    whens = [(1, 1), (0, 2), (3, 3), (2, 4), (-1, 5)]
    print(dict(whens))