class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        for (const num of nums) {
            const selected = nums[nums.length - 1];
            const remainingElemnts = nums.pop();
            if (nums.includes(selected)) {
                return true;
            }
        }
        return false

        // const numSet = new Set();
        // for (const num of nums) {
        //     if (numSet.has(num)) {
        //         return true;
        //     }
        //     numSet.add(num);
        // }
        // return false;
    }
}
