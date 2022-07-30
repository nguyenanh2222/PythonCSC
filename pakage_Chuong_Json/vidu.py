import json
import urllib.request
url1 = 'https://api.github.com/users?since=100'

DEFAULT_ENCODING = 'utf-8'
url = 'https://api.github.com/users?since=100'
urlResponse = urllib.request.urlopen(url)

if hasattr(urlResponse.headers, 'get_content_charset'):
    encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
else:
    encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING

noi_dung = json.loads(urlResponse.read().decode(encoding))

for item in noi_dung:
    print(item['avatar_url'])
    print("\n")