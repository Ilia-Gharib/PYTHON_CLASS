def gcd(a, b):
    """این تابع بزرگ‌ترین مقسوم‌علیه مشترک (GCD) دو عدد را پیدا می‌کند."""
    while b != 0:
        a, b = b, a % b  # الگوریتم اقلیدس
    return abs(a)  # مقدار GCD همیشه باید مثبت باشد

# تست تابع
try:
    number1 = int(input("عدد اول را وارد کنید: "))
    number2 = int(input("عدد دوم را وارد کنید: "))

    result = gcd(number1, number2)
    print(f"بزرگ‌ترین مقسوم‌علیه مشترک {number1} و {number2} برابر است با: {result}")
except ValueError:
    print("لطفاً یک عدد صحیح وارد کنید.")