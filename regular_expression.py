"""
- regular expresstion pattern
 + math()
 +search()
 ---> viet tat regex
"""

import re
line = "the wheels on the bus go round and round, round and round, round and round"
match_obj1 = re.match(r'(.*) go (.*?) .*?', line, re.M|re.I)
if match_obj1:
    print(match_obj1.group())
    print(match_obj1.group(1))
    print(match_obj1.group(2))
    print(match_obj1.groups())
else:
    print("No match")
match_obj2 = re.match(r'(.*) wheels (.*?) .*', line, re.M|re.I)
if match_obj2:
    print(match_obj2.group())
    print(match_obj2.group(1))
    print(match_obj2.group(2))
    print(match_obj2.groups())
else:
    print("No match")

phone = "(08) 38-351056 # This is Phonbe Number"
num = re.sub(r'#.*$', "", phone)
print(num)
num = re.sub(r'\D', "", phone)
print(num)

text = "There are five apples on the table"
word = re.findall(r"\b\w{5}\b", text)
print(word)