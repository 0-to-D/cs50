import sys

if len(sys.argv)<2:
      sys.exit("too few args")
    
for input in sys.argv[1:]:
    print(f"{input}")
