rezult=0
while True:

    num=int(input("enter number:"))
    if num==0:
        print("your out")
        print(f"your rezult is :{rezult}")
        break;
    else:
        num**=3
        rezult+=num
        print(f"yor cube :{num}")
        
           