import string as s
from random import *

ch = s.ascii_letters + s.digits + s.punctuation
password = "".join(choice(ch) for x in range(randint(16, 16)))

print(password)
