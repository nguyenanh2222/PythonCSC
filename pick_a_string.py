import re
def find(str_input: str, str_fining: str):
        if re.search(r'(.*)'+str_fining+'(.*)', str_input, re.M|re.I) is not None:
            return re.search(r'(.*)'+str_fining+'(.*)', str_input, re.M|re.I)
        else:
            return None

if __name__=="__main__":
    str_input = input()
    print(find(str_input, 'anh'))

