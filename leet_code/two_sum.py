from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
	hash_map = {i: num for i, num in zip(nums, range(0, len(nums)))}

	next_num = 1
	for i, num in enumerate(nums):
		comp = target - num
		if comp in nums[next_num:]:
			return [i, hash_map[comp]]
		next_num += 1

