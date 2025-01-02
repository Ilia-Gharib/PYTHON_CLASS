name = []
ave  = []
cood = []
x=0

def add_student():
        global x
        n = input("enter name of student : ")
        a = input("enter avrage of student : ")
        c = input("enter cood of student : ")
        x =+1
        name.append(n)
        ave.append(a)
        cood.append(c)
        print("=====================================================")


def display():
    print("{0:10s}{1:10s}{2:10s}".format("Name", "Average", "Code"))
    print("----------------------------------------")
    for i in range(len(name)): 
        print("{0:10s}{1:10s}{2:10s}".format(name[i], ave[i], cood[i]))
    print("=====================================================")
        
def maxim_student():
    maxi=max(ave)
    indmaxi=ave.index(maxi)
    print(f"max avrage is {maxi} for {name[indmaxi]} ")
    print("=====================================================") 
 
def minim_student():
    mini=min(ave)
    indmin=ave.index(mini)
    print(f"mim avrage is{mini} for {name[indmin]} ")
    print("=====================================================")  

def delete_student():
    D = int(input("what cood you want to delete : "))
    for i in range(x):
            if cood[i] == D:
                print("the student {name[i]} deleting of list ...")
                cood.remove(i)
                name.remove(i)
                ave.remove(i)
                print("delete is complat")
    print("=====================================================")        
    print("{0:10s}{1:10s}{2:10s}".format("name","avrage","cood"))
    print("------------------------------")
    for i in range(x):
        print("{0:10s}{1:10s}{2:10s}".format(name[i],ave[i],cood[i]))
            

     
def meno():
    print("add student enter 1 ")
    print("delete student enter 2 ")
    print("maximo ave student enter 3 ")
    print("minimom ave student enter 4 ")
    print("display all 5 ")
    print("exit enter 6 ")    
    while True :
        ch=input("\n pleas enter what do you want : ")
        if ch == "1":
            add_student()
        elif ch =="2":
            delete_student()
        elif ch =="3":
            maxim_student()
        elif ch =="4":
            minim_student()
        elif ch =="5":
            display()
        elif ch =="6":
            print("exiting ...")
            break
        else:
            print("pleas enter number 1.2.3.4.5")



if __name__ == "__main__":
   meno()    
