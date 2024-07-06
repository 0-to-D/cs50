def main():
    name = input("whats youur name" )
    print(hello(name))

def hello(to="world"):
    return f"hellow {to}"

if __name__ == "__main__":
    main()
