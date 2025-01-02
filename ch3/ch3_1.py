num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
def large_number(num1,num2,num3):
    max_value=num1;
    if num2>max_value:
        max_value=num2
    if num3>max_value:
        max_value=num3
        return max_value;
    print(f"largest number:{max_value}")
large_number(num1, num2, num3)
    
    