"""

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

"""
from typing import List


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		start at the back of each list

		use 3 pointers
		p1 = m -1
		p2 = n -1
		p3 = (m+n) IE the length of nums1


		start the back of each array
		check if nums1[p1] < nums2[p2]  if so add nums2[p2] to back of nums1 IE nums1[p3]
		decrease p2 by one to check the next element in nums2 against nums1[p1]
		and vise versa
		decrease p3 by one each time
		keep going till p3 = 0
		if

		"""
		if n == 0:
			return
		if m == 0:
			p1, p2, p3 = m, n - 1, (n + m) - 1
		if m > 0:
			p1, p2, p3 = m - 1, n - 1, (n + m) - 1

		while p2 >= 0 and p1 >= 0 and p3 >= 0:
			if p1 >= 0 and nums1[p1] < nums2[p2]:
				nums1[p3] = nums2[p2]
				p2 -= 1
			else:
				nums1[p3] = nums1[p1]
				p1 -= 1
			p3 -= 1

solution = Solution()

solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3 )

