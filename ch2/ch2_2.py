num=0;
i=0;
for num in range(10):
    num=int(input(f"enter number{num+1}:"))
    if num % 4 ==0:
        i+=1;
        print(f"yor number %4:{i}")