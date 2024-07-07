balance = 0

def main():
    print(balance)
    increment(100)
    print(balance)
    decrement(50)
    print(balance)

def increment(n):
    global balance
    balance += n

def decrement(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
