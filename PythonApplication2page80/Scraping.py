
#scraping

import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/index.php\?title=List_of_Game_of_Thrones_episodes&oldid=802553687'    #In debug & Fiddler fails

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

#All fails with Fiddler in debug?

import requests
#url = 'http://www.webscrapingfordatascience.com/usercheck/'  #This works
url='http://cnn.com'
url='https://www.GlobeTax.com'
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' + ' (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

r = requests.get(url, headers=my_headers)
print(r.text)
print(r.request.headers)

print(r.headers)

html_contents = r.text
html_soup = BeautifulSoup(html_contents,"html.parser")

import datetime

#d = datetime.datetime.strptime( "20170108233000", "%Y%m%d%H%M%S")
#d = datetime.datetime.strptime( str(datetime.datetime.now()),"YYYY%m%d%H%M%S")    2021-08-23 10:36:54.240988

#ticks=d.timestamp()
#fileName=str(ticks) +".html"

#t0 = datetime.datetime(1970, 1, 1, tzinfo=timezone.utc)
#ticks = (d - t0).total_seconds()


fileName=str(datetime.datetime.now())[17:19] +".html"
MyText= r.text

with open(fileName, "w", encoding = 'utf-8') as f:
	f.write(str(html_soup.prettify()))
	# works too f.write(str(html_soup))

#f=open(fileName,"a")
#f.write(MyText)   #'charmap' codec can't encode character '\uf102' in position 39699: character maps to <undefined>


f.close()

#https://www.geeksforgeeks.org/how-to-write-the-output-to-html-file-with-python-beautifulsoup/?ref=rp