
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
 
print(r.reason)
 
print(r.headers)

#-----------------------------------------------------------------------------------------------
import requests
#url = 'http://www.webscrapingfordatascience.com/usercheck/'  #This works
url = 'https://en.wikipedia.org/w/index.php\?title=List_of_Game_of_Thrones_episodes&oldid=802553687'    #This doesnot
url = 'https://www.target.com'
url='https://www.GlobeTax.com'
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' + ' (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

r = requests.get(url, headers=my_headers)
print(r.text)
print(r.request.headers)

print(r.headers)

#All fails with Fiddler