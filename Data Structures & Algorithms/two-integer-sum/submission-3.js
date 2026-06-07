class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const twoSum = [];

        for (let i = 0; i < nums.length; i++) {
            for (let j = 0; j < nums.length; j++) {
                if (nums[i] + nums[j] === target && i !== j) {
                    if (nums[i] < nums[j]) {
                        twoSum[0] = i;
                        twoSum[1] = j;
                    }
                    else {
                        twoSum[0] = j;
                        twoSum[1] = i;
                    }
                }
            }
        }
        return twoSum;
    }
}