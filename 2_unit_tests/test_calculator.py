from calculator import squr

def test_positive():
    assert squr(2) == 4
    assert squr(3) == 9
    
def test_zero():
    assert squr(0) == 0
    
def test_negative():
    assert squr(-2) == 4
    assert squr(-5) == 25

def main():
    test_positive()
    test_negative()
    test_zero()


if __name__ == "__main__":
    main()
