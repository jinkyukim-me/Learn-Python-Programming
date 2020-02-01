# import URL

import urllib.request as r
with r.urlopen('http://python.org/') as response:
    html = response.read()

response = r.urlopen('http://python.org/')
html = response.read()

print(html)

