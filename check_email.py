import re


def check_mail(email: str):
    if re.match(r'^[a-zA-Z0-9_!#$%&’*+/=?`{|}~^.-]+@[a-z0-9.-]+\.[a-z]{2,3}$', email):
        return True
    else:
        return False


if __name__ == "__main__":
    email = input("Nhap dia chi email: ")
    print(check_mail(email))
