"""
Question 4
Write a Python program to get the top stories from Google news.

Author: Rushabh Barbhaya
"""

import requests
from bs4 import BeautifulSoup

class QuestionFour:
	"""
	Question 4: Write a Python program to get the top stories from Google news.
	To solve this, we are using the RSS feed of google news
	Author: Rushabh Barbhaya
	"""
	def __init__(self, url):
		response = requests.get(url=url)
		if response.status_code == 200:
			news_list = BeautifulSoup(response.text, "xml").findAll("item")
			for news in news_list:
				print(f"TITLE:\t\t{news.title.text}\nURL:\t\t{news.link.text}\nTimeStamp:\t{news.pubDate.text}")
				print("-"*60)



QuestionFour(url='https://news.google.com/news/rss')