import numpy as np 
def sum_matrix(ma,mb):
     return ma+mb
 
n=int(input("Enter the number of columns (n):"))
m=int(input("Enter the number of row (m):"))
 
print("Enter the value for matrix A :")
matrix_a=[]
for i in range(m):
    row=[]
    for j in range(n):
         val=int(input(f"Enter value for element ({i},{j}) : "))
         row.append(val)
    matrix_a.append(row)
matrix_a=np.array(matrix_a)    

print("Enter the value for matrix B :")
matrix_b=[]
for i in range(m):
     row=[]
     for j in range(n):
         val=int(input(f"Enter value for element ({i},{j}) : "))
         row.append(val)
     matrix_b.append(row)
matrix_b=np.array(matrix_b)  


sums_mtx = sum_matrix(matrix_a,matrix_b)
print(" the sum of matrices A and B is :")
print(sums_mtx)