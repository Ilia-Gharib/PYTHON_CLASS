n=int(input("enter number student:"))
avg=[]
for i in range(n):
    num=float(input(f"enter your grade{i+1}:"))
    avg.append(num)
total_avg= sum(avg)/n
print(f"average:{total_avg}")
up_avg=0
low_avg=0
for num in avg:
    if num>total_avg:
        up_avg+=1
    elif num<total_avg:
        low_avg+=1

print("max",up_avg) 
print("min",low_avg)