import requests   #works with fiddler in or without Debug mode
url = 'http://www.webscrapingfordatascience.com/trickylogin/'
my_session = requests.Session()
#Chapter 4 Delving Deeper in HTTP 120
r = my_session.post(url)
r = my_session.post(url, params={'p': 'login'}, data={'username': 'dummy', 'password': '1234'})
r = my_session.get(url, params={'p': 'protected'})
print(r.text)
# Shows: Here is your secret code: 3838.
