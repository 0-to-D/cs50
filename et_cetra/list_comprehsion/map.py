def main():
    caps("yo", "wassup", "np")
    map_caps("noo", "otjtk", "jdbsksj")

def caps(*words):
    sentence = []
    for each in words:
        sentence.append(each.upper())
    print(*sentence)

def map_caps(*words):
    sentence = map(str.upper, words)
    sentence2 = [word.upper() for word in words]
    print(*sentence,"\n", *sentence2)

if __name__ == "__main__":
    main()

