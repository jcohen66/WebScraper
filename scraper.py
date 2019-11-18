import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Interchangeable-Digital-28-70mm-Accessory/dp/B00R1P93SC/ref=sr_1_1_sspa?keywords=sony+a7&qid=1573959945&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRzUyVkpEQUU3UkpWJmVuY3J5cHRlZElkPUEwMjkxMjU3Q0xGWU1YMUdBTUxMJmVuY3J5cHRlZEFkSWQ9QTEwMzI1NzMzTzJOUkQyUVBHMkhUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.97 Chrome/78.0.3904.97 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
print(title)

print(soup.prettify())