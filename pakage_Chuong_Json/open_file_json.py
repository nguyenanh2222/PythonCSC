import urllib.request
import json
def dump_json_from_internet_unicode(url):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urllib.request.urlopen(url)
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    data = json.loads(urlResponse.read().decode(encoding))
    return data
