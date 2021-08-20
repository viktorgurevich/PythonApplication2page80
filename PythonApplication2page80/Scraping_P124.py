import requests


url = 'http://www.webscrapingfordatascience.com/cookielogin/'
# First perform a POST request
r = requests.post(url, data={'username': 'dummy', 'password': '12345'})
# Get the cookie value, either from
# r.headers or r.cookies print(r.cookies)
my_cookies = r.cookies
# r.cookies is a RequestsCookieJar object which can also
# be accessed like a dictionary. The following also works:
my_cookies['PHPSESSID'] = r.cookies.get('PHPSESSID')
# Now perform a GET request to the secret page using the cookies
r = requests.get(url + 'secret.php', cookies=my_cookies)
print(r.text)
# Shows: This is a secret code: 1234
