numbers = []
negative_numbers = []

n = int(input("enter of number value: "))
for i in range(n):
    num=int(input(f"enter number {i+1}:"))
    numbers.append(num)
for num in numbers:
    if num<0:
        negative_numbers.append(num)

#numbers = [num for num in numbers if num >= 0]



print(f"plus number:{numbers}")
print(f"negative numbers:{negative_numbers}")
