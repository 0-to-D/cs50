import sys

if len(sys.argv) == 1:
    print("no args ")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    for _ in range(int(sys.argv[2])):
        print("meaw")
else:
    print("usage: meaw")
