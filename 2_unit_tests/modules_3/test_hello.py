from hello import hello

def test_default():
    assert hello() == "hellow eworld"

def test_args():
    assert hello("tomu" == "hellow tomu")

'''
def main():
    test_default()
    test_args()

if __name__ == "__main__":
    main()
'''
