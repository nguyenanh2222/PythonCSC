
import urllib.request
import json
def read_json_from_internet_unicode(url):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urllib.request.urlopen(url)
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    data = json.loads(urlResponse.read().decode(encoding))
    return data
def display_item_tivi(url):
    data = read_json_from_internet_unicode(url)
    for item in data['Danh_sach_Tivi']:
        print(item)

def display_item(url):
    data = read_json_from_internet_unicode(url)
    data['ten_san_pham']
    data['hinh_san_pham']
    data['']




if __name__ == "__main__":
    url1 = 'http://api.laptrinhpython.net/san-pham'
    url2 = 'http://api.laptrinhpython.net/tivi'
    print(read_json_from_internet_unicode(url2))