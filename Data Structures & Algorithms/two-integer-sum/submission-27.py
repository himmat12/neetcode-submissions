class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        for i, num in enumerate(nums):
            arr.append([num, i])

        arr.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            current_sum = arr[i][0] + arr[j][0]
            if current_sum == target:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        return []
