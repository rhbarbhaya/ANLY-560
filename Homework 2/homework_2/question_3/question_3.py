class QuestionThree:
    """
    Question:
    Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
    Author: Rushabh Barbhaya
    """
    def __init__(self, num: int) -> None:
        """
        Default function to check if the number is integer and satisfies the condition
        :param num: input number from the script
        :type num: int
        """
        if not isinstance(num, int):
            raise ValueError(f"Expect integers, {num} is not an interger")
        else:
            if (num > (4**4)) and ((num % 34) == 4):
                print(f"Number {num} accepted")
            else:
                print(f"{num} is an invalid number")


QuestionThree(16)  # Initiate for question 3 and check 1
QuestionThree(922)   # Check 2
QuestionThree(914)  # Check 3
QuestionThree(0)  #  Check 4