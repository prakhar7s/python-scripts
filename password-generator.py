import string
import random

letters = string.digits
digits = string.digits
special_symbols = '@#$%&*<>{}[]()'

all = letters + digits + special_symbols

length = int(input('Password Length: '))

password = "".join(random.sample(all, length))
print(password)
