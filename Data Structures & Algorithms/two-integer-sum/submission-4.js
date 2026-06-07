class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            const compliment = target - num;
            const sumIndex = map.get(compliment);

            if (map.has(compliment)) {
                return [i, sumIndex];
            }
            map.set(num, i);
        }
        return [];
    }
}