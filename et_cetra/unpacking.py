def total1(a, b, c):
    return a+b+c

def total2(a,b,c):
    return a+b+c

lst1 = [5, 10, 15]

lst2 = {"a": 10, "b": 20, "c": 30}

print(total1(*lst1))
#print(f"(lst2)")
print(total2(**lst2))
