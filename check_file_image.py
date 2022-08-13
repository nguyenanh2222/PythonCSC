import re


def check_file_ending(filename: str):
    if re.match(r'(^([A-Za-z0-9._%+-]+(\.(jpg|png|gif|bmp))$))', filename, re.M | re.I):
        return True
    else:
        return False


if __name__ == "__main__":
    filename = input("Nhap ten file: ")
    print(check_file_ending(filename))
