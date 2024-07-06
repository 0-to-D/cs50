def main():
    name = get_name() #get name function eeturned a tuple immutable
    print(f"{name[0]} {name[1]}")

def get_name():
    name = input("name")
    grade = input("grade")
    return (name, grade)

if __name__ == "__main__":
    main()
