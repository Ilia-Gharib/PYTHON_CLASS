import math as math

a=float(input("enter number a:"))
b=float(input("enter number b:"))
c=float(input("enter number c:"))

if a == 0:
    print("a !=0")
else:
    delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"root:x1{x1}and x2{x2}")
elif delta == 0:
        x = -b / (2 * a)
        print(f"root: x = {x}")
else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"all root: x1 = {real_part} + {imaginary_part}i and x2 = {real_part} - {imaginary_part}i")