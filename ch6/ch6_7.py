number=[]
number2=[]

for i in range(20):
    num=int(input("enter  your number (1-100):"))
    number.append(num)
print("this first number in list  :",number)
fix_num=set(number)
number2.append(fix_num)
print("this next number in list ",number2)  