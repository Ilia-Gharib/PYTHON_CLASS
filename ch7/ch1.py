
class rational:
    def __init__(self,kasr_1,kasr_2):
        k_1 = kasr_1.split("/")# 2 / 3
        k_2 = kasr_2.split("/")
        self.sk_1 = int(k_1[0])
        self.mk_1 = int(k_1[1])
        self.sk_2 = int(k_2[0])
        self.mk_2 = int(k_2[1])
         
    def sum(self):
        if (self.mk_1 == self.mk_2):
            print(f"sum of tow kasr = {self.sk_1 + self.sk_2}/{self.mk_2}")
        else:
            mk_x = self.mk_1 * self.mk_2
            r1 = (self.sk_1 * self.mk_2)
            r2 = (self.sk_2 * self.mk_1)
            rb=r1+r2
            print(f"sum of tow kasr = {rb}/{mk_x}")
            
            
    def minn(self):
            if (self.mk_1 == self.mk_2):
                print(f"minn of tow kasr = {self.sk_1 - self.sk_2}/{self.mk_2}")
            else:
                mk_x = self.mk_1 * self.mk_2
                r1 = (self.sk_1 * self.mk_2)
                r2 = (self.sk_2 * self.mk_1)
                rb=r1-r2
                print(f"sum of tow kasr = {rb}/{mk_x}")
                
    def zarb(self):
        print(f"zarb of tow kasr = {self.sk_1 * self.sk_2}/{self.mk_1 *self.mk_2}")
    def tagsim(self):
        print(f"zarb of tow kasr = {self.sk_1 * self.mk_2}/{self.mk_1 *self.sk_2}")
            

def meno():
    kasr_1 = input("enter kasr 1 for exampel x/y : ")
    kasr_2 = input("enter kasr 2 for exampel x/y : ")
    print("if you want exit type x")
    while True:
        ch = input("enter / * + - : ")
        if ch == "/":
            call = rational(kasr_1,kasr_2)
            call.tagsim()
        elif ch == "*":
            call = rational(kasr_1,kasr_2)
            call.zarb()
        elif ch == "+":
            call = rational(kasr_1,kasr_2)
            call.sum()
        elif ch == "-":
            call = rational(kasr_1,kasr_2)
            call.minn()
        elif ch == "x":
            print("exiting ...")
            break
        else:
            print("just iter / * + - : ")
            
if __name__ == "__main__":
    meno()
            
         
        
    