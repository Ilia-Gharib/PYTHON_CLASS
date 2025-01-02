import mysql.connector

# اتصال به پایگاه داده
db = mysql.connector.connect(
    host="localhost",
    user="your_username",  # نام کاربری خود را وارد کنید
    password="your_password",  # رمز عبور خود را وارد کنید
)

cursor = db.cursor()

# الف. ایجاد پایگاه داده
cursor.execute("CREATE DATABASE IF NOT EXISTS university")
cursor.execute("USE university")

# ب. ایجاد جدول دانشجویان
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    gpa FLOAT
)
""")

# ب. وارد کردن اطلاعات رکورد از کاربر
n = int(input("enter n: "))

students_data = []

for _ in range(n):
    student_id = int(input("enter code student: "))
    name = input("name : ")
    gpa = float(input("avg student : "))
    students_data.append((student_id, name, gpa))

# وارد کردن داده‌ها به جدول
cursor.executemany("INSERT INTO students (student_id, name, gpa) VALUES (%s, %s, %s)", students_data)
db.commit()

# پ. بازیابی رکورد خاصی از جدول
student_id_to_find = int(input("enter code student for serch: "))
cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id_to_find,))
student_record = cursor.fetchone()
print("رکورد دانشجو:", student_record)

# ت. بازیابی دانشجویانی که معدل آنها بین 12 و 17 است
cursor.execute("SELECT * FROM students WHERE gpa BETWEEN 12 AND 17")
students_in_range = cursor.fetchall()
print("student evg betwen 12 to 17:", students_in_range)

# ث. پیدا کردن دانشجویی با شماره دانشجویی 100 و تغییر معدل به 19
student_id_to_update = 100
cursor.execute("UPDATE students SET gpa = 19 WHERE student_id = %s", (student_id_to_update,))
db.commit()

# بررسی تغییر
cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id_to_update,))
updated_student = cursor.fetchone()
print("student update:", updated_student)

# بستن اتصال
cursor.close()
db.close()