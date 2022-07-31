import json
import urllib.request


def read_json_api_unicode(url):
    """doc: Doc va gi noi dung file json"""
    DEFAULT_ENCODING = "UTF-8"
    urlResponse = urllib.request.urlopen(url)
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    data = json.loads(urlResponse.read().decode(encoding))
    return data


def display_headers():
    print("STT"
          '{:10}'.format('Tên sản phẩm')
          '{:40}'.format('Hình sản phẩm')
          '{:10}'.format('Giá size S')
          '{:10}'.format('Giá size M'))


if __name__ == "__main__":
    data = read_json_api_unicode('http://api.laptrinhpython.net/san-pham')
    print(data)
    display_headers()
    i = 1
    for item in data:
        print(i, item['ten_san_pham'].ljust(20))
        i += 1
