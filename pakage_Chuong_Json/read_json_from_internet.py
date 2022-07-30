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
    print("STT" +
          '{:<5}'.format('') + "Tên sản phẩm" +
          '{:<20}'.format('') + "Hình sản phẩm" +
          '{:<15}'.format('') + "Giá size S" +
          '{:<10}'.format('') + "Giá size M")


if __name__ == "__main__":
    data = read_json_api_unicode('http://api.laptrinhpython.net/san-pham')
    # print('{:<10}'.format("STT","Tên sản phẩm", "Hình sản phẩm", "Giá size S", "Giá size M"))
    # hears = (,"Tên sản phẩm", "Hình sản phẩm", "Giá size S", "Giá size M")
    # for item in hears:
    display_headers()
    i = 1
    for item in data:
        print(i,
              '{:<5}'.format('') + item['ten_san_pham'], item['hinh_san_pham'].ljust(50))
        # print('{:<70}'.format('') + (item['gia_size_s']).rjust(50))
        # print('{:<100}'.format('') + str(item['gia_size_m']))
        i += 1
