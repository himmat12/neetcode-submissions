class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.isalnum():
                arr.append(c.lower())
        res = True
        l = 0
        r = len(arr) - 1
        print(arr)
        while l <= r:
            print(l, r)
            if arr[l] != arr[r]:
                res = False
                break
            l += 1
            r -= 1
        return res
