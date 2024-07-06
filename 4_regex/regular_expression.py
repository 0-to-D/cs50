import re

email = input("wnter email  ").strip()

if re.search(r"^[^$]+@[^$]+\.com$", email):#r is Raw String
    print("valid")
else:
    print("invalid")
