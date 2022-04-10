"""
Question 1:
Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.

Author: Rushabh Barbhaya
"""

from collections import Counter
from ast import literal_eval


class QuestionOne:
    """
    Class for Question 1. Intention is to use some functions for other classes wherever applicable
    Question1:
    Write a Python function that takes a sequence of numbers and determines
    whether all the numbers are different from each other.
    """
    @staticmethod
    def is_number_check(nums: list) -> list:
        """
        Function to convert a string list to an int or float list. This function takes the list literally.
        Checks in the function:
        - Checks if the input is a list
        - Checks if there are inputs in the form of a string, converts them to literal values
        - If error, breaks the code with the error type
        :param nums: Should be a list of Numbers and converts numbers that are in the form of a string to numbers
        :type nums: list
        :return: corrected list of numbers
        :rtype: list
        """
        if not isinstance(nums, list):  # Checks if the input argument is a list
            raise TypeError("Invalid input argument. Please enter a iterable type")
        if any(str(num).isdigit() for num in nums):  # Converts the numbers in string form to numbers
            new_nums: list = []
            for num in nums:
                try:
                    if isinstance(literal_eval(num), (int, float)):
                        new_nums.append(literal_eval(num))
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
            dupes: dict = Counter(nums)
            dupes: set = {k for k, v in dupes.items() if v > 1}
            print(f"There are duplicate(s) in the input list {nums} -> duplicates: {dupes}")



class QuestionTwo:
    """
    Question:
    Write a Python program find a list of integers with exactly two occurrences
    of nineteen and at least three occurrences of five.
    """
    def __init__(self, nums) -> None:
        """
        Check for occurrences for the given scope.
        Scope defaults to 2 or more counts of 19 and 3 or more counts of 5

        This function also inherits the list check from question 1
        :param nums: gets a list of numbers
        :type nums: list
        :return:
        :rtype:
        """
        nums: list = QuestionOne.is_number_check(nums)
        nums_dict = Counter(nums)
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


class QuestionThree:
    """
    Question 3:
    Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
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


import requests
from bs4 import BeautifulSoup

class QuestionFour:
    """
    Question 4: Write a Python program to get the top stories from Google news.
    To solve this, we are using the RSS feed of google news
    """
    def __init__(self, url):
        response = requests.get(url=url)
        if response.status_code == 200:
            news_list = BeautifulSoup(response.text, "xml").findAll("item")
            for news in news_list:
                print(f"TITLE:\t\t{news.title.text}\nURL:\t\t{news.link.text}\nTimeStamp:\t{news.pubDate.text}")
                print("-"*60)

# Initiate the class variable for question 1
unique_test = QuestionOne()
unique_test.is_unique([1, 2, 4, 5, 5, 7, 3])  # Check 1
"""
Output:
There are duplicate(s) in the input list [1, 2, 3, 4, 5, 5, 7] -> duplicates: {5}
"""
unique_test.is_unique(["1", "2.4", 6])  # Check 2
"""
Output:
All unique values in the list, length of list 3
"""
unique_test.is_unique([1, 1.0])  # Check 2
"""
Output:
There are duplicate(s) in the input list [1, 1.0] -> duplicates: {1}
"""

# Initiate the class varaibale for question 2
QuestionTwo([19, 12, 19])  #Check 1
"""
Output:
Conditions met for key 19 ::: Index = [0, 2]
"""
QuestionTwo([5, 12, 19, 5])  # Check 2
"""
Output:
Conditions are not for [19, 5]
"""
QuestionTwo([5,5,5,19,7])  # Check 3
"""
Output:
Conditions met for key 5 ::: Index = [0, 1, 2]
"""
QuestionTwo([5, 12, 19, 5, 8, 190, 19, 50, 5])  # Check 4
"""
Output:
Conditions met for key 19 ::: Index = [2, 6] & Conditions met for key 5 ::: Index = [0, 3, 8]
"""
QuestionTwo(["19", 12, 19])  # Check 5
"""
Output
Conditions met for key 19 ::: Index = [0, 2]
"""

# Initiate for question 3
QuestionThree(16)  # check 1
"""
16 is an invalid number
"""
QuestionThree(922)   # Check 2
"""
Number 922 accepted
"""
QuestionThree(914)  # Check 3
"""
914 is an invalid number
"""
QuestionThree(0)  #  Check 4
"""
0 is an invalid number
"""

# Initialization for question 4
QuestionFour(url='https://news.google.com/news/rss')
"""
Partial Output:
TITLE:		UK pledges new military assistance for Ukraine after PM's surprise visit to Kyiv - CNN
URL:		https://news.google.com/__i/rss/rd/articles/CBMiUmh0dHBzOi8vd3d3LmNubi5jb20vMjAyMi8wNC8wOS9ldXJvcGUvdWtyYWluZS11ay1ib3Jpcy1qb2huc29uLWludGwtZ2JyL2luZGV4Lmh0bWzSAVZodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDIyLzA0LzA5L2V1cm9wZS91a3JhaW5lLXVrLWJvcmlzLWpvaG5zb24taW50bC1nYnIvaW5kZXguaHRtbA?oc=5
TimeStamp:	Sat, 09 Apr 2022 21:22:00 GMT
------------------------------------------------------------
TITLE:		Russia-Ukraine war: What happened today (April 9) - NPR
URL:		https://news.google.com/__i/rss/rd/articles/CBMiWGh0dHBzOi8vd3d3Lm5wci5vcmcvMjAyMi8wNC8wOS8xMDkxNjkxMTA1L3J1c3NpYS11a3JhaW5lLXdhci13aGF0LWhhcHBlbmVkLXRvZGF5LWFwcmlsLTnSAQA?oc=5
TimeStamp:	Sat, 09 Apr 2022 20:27:32 GMT
------------------------------------------------------------
TITLE:		Pakistan Leader Imran Khan Is Dismissed After No-Confidence Vote Loss - The Wall Street Journal
URL:		https://news.google.com/__i/rss/rd/articles/CBMic2h0dHBzOi8vd3d3Lndzai5jb20vYXJ0aWNsZXMvc3VwcG9ydGVycy1vZi1wYWtpc3RhbnMtaW1yYW4ta2hhbi1kZWZ5LXRvcC1jb3VydC1ibG9jay12b3RlLWluLXBhcmxpYW1lbnQtMTE2NDk1MjI1NTjSAXdodHRwczovL3d3dy53c2ouY29tL2FtcC9hcnRpY2xlcy9zdXBwb3J0ZXJzLW9mLXBha2lzdGFucy1pbXJhbi1raGFuLWRlZnktdG9wLWNvdXJ0LWJsb2NrLXZvdGUtaW4tcGFybGlhbWVudC0xMTY0OTUyMjU1OA?oc=5
TimeStamp:	Sat, 09 Apr 2022 23:28:00 GMT
------------------------------------------------------------
TITLE:		Police: Owner, wife, grandson shot dead in robbery at Coweta gun range -  The Atlanta Journal Constitution
URL:		https://news.google.com/__i/rss/rd/articles/CBMifmh0dHBzOi8vd3d3LmFqYy5jb20vbmV3cy9jcmltZS9wb2xpY2Utb3duZXItd2lmZS1ncmFuZHNvbi1zaG90LWRlYWQtaW4tcm9iYmVyeS1hdC1jb3dldGEtZ3VuLXJhbmdlL0pRNElJWTZQRFJENjNGNzM1NEFHV0hTRjVJL9IBjQFodHRwczovL3d3dy5hamMuY29tL25ld3MvY3JpbWUvcG9saWNlLW93bmVyLXdpZmUtZ3JhbmRzb24tc2hvdC1kZWFkLWluLXJvYmJlcnktYXQtY293ZXRhLWd1bi1yYW5nZS9KUTRJSVk2UERSRDYzRjczNTRBR1dIU0Y1SS8_b3V0cHV0VHlwZT1hbXA?oc=5
TimeStamp:	Sat, 09 Apr 2022 20:48:45 GMT
------------------------------------------------------------
TITLE:		China Is Accelerating Its Nuclear Buildup Over Rising Fears of U.S. Conflict - The Wall Street Journal
URL:		https://news.google.com/__i/rss/rd/articles/CBMidGh0dHBzOi8vd3d3Lndzai5jb20vYXJ0aWNsZXMvY2hpbmEtaXMtYWNjZWxlcmF0aW5nLWl0cy1udWNsZWFyLWJ1aWxkdXAtb3Zlci1yaXNpbmctZmVhcnMtb2YtdS1zLWNvbmZsaWN0LTExNjQ5NTA5MjAx0gF4aHR0cHM6Ly93d3cud3NqLmNvbS9hbXAvYXJ0aWNsZXMvY2hpbmEtaXMtYWNjZWxlcmF0aW5nLWl0cy1udWNsZWFyLWJ1aWxkdXAtb3Zlci1yaXNpbmctZmVhcnMtb2YtdS1zLWNvbmZsaWN0LTExNjQ5NTA5MjAx?oc=5
TimeStamp:	Sat, 09 Apr 2022 13:00:00 GMT
------------------------------------------------------------
"""