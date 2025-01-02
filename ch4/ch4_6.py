# تابع مرتب‌سازی و ادغام دو آرایه
def merge_sorted_arrays(arr1, arr2):
    merged_array = sorted(arr1 + arr2)  # ترکیب دو آرایه و مرتب‌سازی
    return merged_array

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:  
                arr[i], arr[j] = arr[j], arr[i]
    return arr


n1 = int(input("تعداد عناصر آرایه اول را وارد کنید:"))   
array1 = []   
for _ in range(n1):
    num = int(input("عناصر آرایه اول را وارد کنید:"))   
    array1.append(num)  
    


n2 = int(input("تعداد عناصر آرایه دوم را وارد کنید:"))  
array2 = []  
for _ in range(n2):
    num = int(input("عناصر آرایه دوم را وارد کنید:"))
    array2.append(num)  

   
array1 = sort_array(array1)
array2 = sort_array(array2)

result = merge_sorted_arrays(array1, array2)

print("آرایه ادغام شده و مرتب شده:")
print(result)
