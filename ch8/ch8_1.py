import os 
import json

FILENAME = "UNIVERSTE.json"

def load_data():
    if not os.path.exists(FILENAME):
        return [] 
    with open(FILENAME,"r") as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME,"w") as file:
        json.dump(data, file, indent=4)

def add_student():
    stu_update = load_data()  
    id_stu  =  input("enter is the student : ")   
    name_stu  =  input("enter is the nmae : ")   
    family_stu  =  input("enter is the family : ")    
    stu_update.append( { "id:": id_stu ,"name:": name_stu , "family:": family_stu } )
    save_data(stu_update)
    
def edit_student(ioi):
    stu = load_data()
    for i9 in stu:
        if  i9["id:"] == ioi: 
          while True : 
            input("1.edit id and name and family")
            input("2.edit id and name")
            input("3.edit id")
            ch = input("what you want to edit ")
            if ch == "1":
                stu["id:"]=input("enter new id: ")
                stu["name:"]=input("enter new name: ")
                stu["family:"]=input("enter new family: ")
                save_data(stu)
                break
            elif ch == "2":
                stu["id:"]=input("enter new id: ")
                stu["name:"]=input("enter new name: ")
                save_data(stu)
                break
            elif ch == "3":
                stu["id:"]=input("enter new id: ")
                save_data(stu)
                break
        

def dis_student():
    stu = load_data()
    print(stu)


def meno ():
    while True:
        print("\n1. Display all students")
        print("2. Edit a student record")
        print("3. Add a new student")
        print("4. Exit...")
        
        ch = input("what do you want pless enter number : ")
        if ch=="1":
            dis_student()
        elif ch == "2":
            item = input("Enter Student ID to edit: ")
            edit_student(item)
        elif ch == "3":
            add_student()
        elif ch == "4":
            print("exiting...")
            break
        else:
            print("this number ther is not just enter 1 . 2 . 3 . 4")
        
if __name__ == "__meno__":
    meno()
    
    