import sys

if len(sys.argv)>2:
    sys.exit("too many args")

elif len(sys.argv)<2:
    sys.exit("too few args")

else:
    sys.exit(f"the name is {sys.argv[1]}")
