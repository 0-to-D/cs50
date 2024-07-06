email = input("enter email").strip()

username, domain = email.split("@")

if username and "." in domain and domain.endswith(".com"):
    print("okay")
else:
    print("not correct email")
