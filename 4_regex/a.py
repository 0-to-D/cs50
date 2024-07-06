email = input("enter email  ").strip()

if "@" in email and "." in email:
    print("okay")
else:
    print("not a email")
