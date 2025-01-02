n = int(input("تعداد اعداد را وارد کنید: "))
numbers = []

# وارد کردن اعداد
for i in range(n):
    num = int(input("عدد را وارد کنید: "))
    numbers.append(num)

# پیدا کردن عدد با بیشترین تکرار
most_frequent = None
max_count = 0

for i in numbers:
    count = numbers.count(i)  # شمارش تکرار عدد i
    if count > max_count:  # اگر تعداد تکرار بیشتر از تکرار قبلی باشد
        max_count = i

print(f"عدد با بیشترین تکرار: {max_count}")

