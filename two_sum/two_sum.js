/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	const index = {};
	var result = [];
	nums.forEach((num, i) => {
		if (target - num in index) {
			result = [i, index[target - num]];
		} else {
			index[num] = i;
		}
	});
	return result;
};
