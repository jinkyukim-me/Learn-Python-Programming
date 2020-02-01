from urllib.request import urlopen

response = urlopen('http://www.google.com')
print(response.status)

from urllib.request import urlopen as u
response = u('http://www.google.com')
print(response.status)

from urllib.request import Request, urlopen
req = Request('http://www.google.com')
response = urlopen(req)
print(response.status)

from urllib.request import Request as r, urlopen as u
req = r('http://www.google.com')
response = u(req)
print(response.status)

