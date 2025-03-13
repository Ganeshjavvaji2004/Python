a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

if a < b and b < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)

