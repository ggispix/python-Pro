# Task 1

import re
string = 'Rbbbbbr'
pattern = r'^[R](B|b)+[Rr]$'
match = re.match(pattern, string)
if match:
    print(match.group())

# Task 2
string = '9999-9999-9999-9999'
pattern = r'(\d{4}-){3}\d{4}'
match = re.match(pattern, string)
if match:
    print(match.group())

# Task 3
string = 'an_gmailcom'
pattern = r'[a-zA-Z0-9]+([_-]?[a-zA-Z0-9_-{1}]+?)$'
match = re.match(pattern, string)
if match:
    print(match.group())

# Task 4
def check_login(login):
# string = '2v'
    pattern = r'\d[a-zA-Z0-9]{2,10}'
    match = re.match(pattern, login)
    if match:
        return match.group()
    raise ValueError("Invalid login")

print(check_login('wertbk_0'))



