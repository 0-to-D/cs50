import argparse

parser = argparse.ArgumentParser(description="meaw like cat")
parser.add_argument("-n",default=1, help="number of times of meaw", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("maew")
