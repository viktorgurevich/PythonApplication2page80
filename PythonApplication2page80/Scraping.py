
#scraping

import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/index.php\?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)   #manually via Browser it gives content, but via code gives 404
html_contents = r.text
html_soup = BeautifulSoup(html_contents,"html.parser")


url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)
print(r.text)

print(r.status_code)
# What is the textual status code?
print(r.reason)
# What were the HTTP response headers?
print(r.headers)