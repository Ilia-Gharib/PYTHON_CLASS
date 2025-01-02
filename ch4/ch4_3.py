rows = 2
cols = 3


matrix=[]

for i in range(rows):
    x=[]
    for j in range(cols):
        element = int(input(f"enter{[i+1]}{[j+1]} element : "))
        x.append(element)
    matrix.append(x)
    

total=[]
for j in range(cols):
    fof=[]
    for i in range(rows):
        fof.append(matrix[i][j])
    total.append(fof)
    
for x in total:
   print(x)

        