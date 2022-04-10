"""
Question:
Write a Python program find a list of integers with exactly two occurrences
of nineteen and at least three occurrences of five.

Author: Rushabh Barbhaya
"""

import collections

class QuestionTwo:
    """
    Question:
    Write a Python program find a list of integers with exactly two occurrences
    of nineteen and at least three occurrences of five.

    Author: Rushabh Barbhaya
    """
    def get_occurrences(self, nums) -> None:
        """
        Check for occurrences for the given scope.
        Scope defaults to 2 or more counts of 19 and 3 or more counts of 5

        This function also inherits the list check from question 1
        :param nums: gets a list of numbers
        :type nums: list
        :param scope: defines the scope for check. Default count(19) == 2 && count(5) >= 3
        :type scope:
        :return:
        :rtype:
        """
        nums: list = QuestionOne.is_number_check(self, nums)
        nums_dict = collections.Counter(nums)
        checkout = []
        conditions = []
        if nums_dict[19] == 2:
            index = [index for index, value in enumerate(nums) if value == 19]
            checkout.append(f"Conditions met for key 19 ::: Index = {index}")
        else:
            conditions.append(19)
        if nums_dict[5] >= 3:
            index = [index for index, value in enumerate(nums) if value == 5]
            checkout.append(f"Conditions met for key 5 ::: Index = {index}")
        else:
            conditions.append(5)
        if len(conditions) > 1:
            print(f"Conditions are not for {conditions}")
        else:
            print(' & '.join(checkout))

occurrence_test = QuestionTwo()  #  Initiate the class varaibale for question 2
occurrence_test.get_occurrences([19, 12, 19])  # Check 1
occurrence_test.get_occurrences([5, 12, 19, 5])  # Check 2
occurrence_test.get_occurrences([5,5,5,19,7])
occurrence_test.get_occurrences([5, 12, 19, 5, 8, 190, 19, 50, 5])  # Check 3
occurrence_test.get_occurrences(["19", 12, 19])  # Check 4