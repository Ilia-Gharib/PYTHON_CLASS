bank_tracotion = ()

def bank(id,name,price,pay):
    global bank_tracotion
    bank_tracotion += ((id, name, price, pay),)



bank("1","ilia","2,000,000","send")
bank("2","ilia","3,000,000","send")
bank("3","ilia","5,000,000","recived")
bank("4","ilia","1,000,000","send")
    
print("{0:10s} {1:10s} {2:10s} {3:10s}".format("id", "name" ,"price" ,"pay"))
print("-"*40)
for i in bank_tracotion:
    print("{0:10s} {1:10s} {2:10s} {3:10s}".format( i[0] , i[1] , i[2], i[3]))