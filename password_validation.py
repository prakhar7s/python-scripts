# 6. A website requires a user to input username and password to register. Write a
# program to check the validity of password given by user. Following are the criteria for
# checking 
# password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 5. Maximum length of transaction 
# password: 12
# PRAKHAR SHRIVASTAVA 0225CS181030

import re

def isValid(inp):
    matches = [r"(.*[a-z].*)",r"(.*[A-Z].*)",r"(.*\d.*)",r"(.*[@#$].*)"]
    for match in matches:
        if not(re.search(match, inp)):
            return "NOT VALID"        
    return "VALID"        
        
inp_user = input("username: ")
inp_pwd = input("password: ")
pwd_len = len(inp_pwd)
ans = isValid(inp_pwd) if pwd_len>=5 and pwd_len<=12 else "NOT VALID"
print(ans)
      
        
