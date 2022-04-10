"""
Question:
Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.

Author: Rushabh Barbhaya
"""

import collections
import ast

class QuestionOne:

    @staticmethod
    def is_number_check(nums: list) -> list:
        """
        Function to convert a string list to an int or float list.
        This function takes the list literally.

        Checks in the function:
            - Checks if the input is a list
            - Checks if there are inputs in the form of a string, converts them to literal values
            - If error, breaks the code with the error type

        param nums: Should be a list of Numbers and converts numbers that are in the form of a string to numbers
        :type nums: list
        :return: corrected list of numbers
        :rtype: list
        """
        if not isinstance(nums, list):  # Checks if the input argument is a list
            raise TypeError("Invalid input argument. Please enter a iterable type")  # If not a list, raise a TypeError
        if any(str(num).isdigit() for num in nums):  # Converts the numbers in string form to numbers
            new_nums: list = []
            for num in nums:
                try:
                    if isinstance(ast.literal_eval(num), (int, float)):
                        new_nums.append(ast.literal_eval(num))
                except ValueError:
                    new_nums.append(num)
            return new_nums
        else:  # Errors if there are any other errors or if there is a non-number character
            raise TypeError("The list contains a non-number character")

    def is_unique(self, nums: list) -> None:
        """
        The main function to check if the list contains unique values. Runs the check first.

        param nums: Expects a list of numbers to check for unique values
        :type nums: list
        :return: Prints the unique or duplicates in the list
        :rtype: None
        """
        nums: list = self.is_number_check(nums)
        nums: list = sorted(nums)
        if len(nums) == len(set(nums)):
            print(f"All unique values in the list, length of list {len(nums)}")
        else:
            dupes: dict = collections.Counter(nums)
            dupes: set = {k for k, v in dupes.items() if v > 1}
            print(f"There are duplicate(s) in the input list {nums} -> duplicates: {dupes}")


unique_test = QuestionOne()  # Initiate the class variable
unique_test.is_unique([1, 2, 4, 5, 5, 7, 3])  # Check 1
unique_test.is_unique(["1", "2.4", 6])  # Check 2
unique_test.is_unique([1, 1.0])  # Check 2
