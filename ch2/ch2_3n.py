number=int(input("enter number:"))

fact=1
for i in range(2,number+1):
    fact*=i

    print(f"factorile{number}:1/{fact}")