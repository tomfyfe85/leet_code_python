import random
import time
from collections import defaultdict


class PalindromeFinder:
	def __init__(self, string_length):
		self.string_length = string_length
		self.string = self._generate_string()

	def _generate_string(self):
		"""
		Generates a random string of digits with a length of self.string_length.
		"""
		string = ''.join(str(random.randint(0, 9)) for _ in range(self.string_length))
		return string

	def get_palindrome_counts_by_length(self):
		"""
		Finds the lengths of all palindromes in the generated string and counts their occurrences.

		:return: A dictionary where the keys are palindrome lengths and the values are the counts of those lengths.
		"""
		palindrome_counts_by_length = defaultdict(int)

		# Code for finding and counting palindromes goes here...
		# (You'll write this logic as part of solving the task yourself)

		return palindrome_counts_by_length

	@staticmethod
	def measure_execution_time(func):
		"""
		Measures and prints the execution time of a given function.

		:param func: The function whose execution time is to be measured.
		"""
		start_time = time.time()
		func()
		end_time = time.time()
		print(f"Execution time: {end_time - start_time:.5f} seconds")


# Example usage:
if __name__ == "__main__":
	# Feel free to change this value
	string_length = 5000
	palindrome_finder = PalindromeFinder(string_length)

	# Print the generated string (for testing)
	print(palindrome_finder.string)

	# Measure execution time of finding palindromes
	PalindromeFinder.measure_execution_time(lambda: print(
		palindrome_finder.get_palindrome_counts_by_length()
	))
