name = []
ave  = []
cood = []

num = int(input("enter number of student : "))
for i in range(num):
    n = input("enter name of student : ")
    a = input("enter avrage of student : ")
    c = input("enter cood of student : ")
    name.append(n)
    ave.append(a)
    cood.append(c)

print("{0:10s}{1:10s}{2:10s}".format("name","avrage","cood"))
print("------------------------------")
for i in range(num):
    print("{0:10s}{1:10s}{2:10s}".format(name[i],ave[i],cood[i]))
print("=====================================================")     
maxi=max(ave)
indmaxi=ave.index(maxi)
mini=min(ave)
indmin=ave.index(mini)

  
print(f"max avrage is {maxi} for {name[indmaxi]} ")
print(f"mim avrage is{mini} for {name[indmin]} ")
print("=====================================================")   
D = int(input("what cood you want to delete : "))
for i in range(num):
    if cood[i] == D:
        print("the student {name[i]} deleting of list ...")
        cood.remove(i)
        name.remove(i)
        ave.remove(i)
        print("delete is complat")
print("=====================================================")        
print("{0:10s}{1:10s}{2:10s}".format("name","avrage","cood"))
print("------------------------------")
for i in range(num):
    print("{0:10s}{1:10s}{2:10s}".format(name[i],ave[i],cood[i]))
    


    
