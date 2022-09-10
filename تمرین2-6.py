# compare x and y
x = int(input("Please enter x :"))
y = 2 * x - 2
print(f"y=2({x})-2={y}")
if x != y:
    print('x<>y', False)
else:
    print('x==y ?', True)
# or
print("\nx<y ?", x < y)
print("x>y ?", x > y)
print("x==y ?", x == y)
