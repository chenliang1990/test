# 父类和子类的定义
class Dada():
    name = "马云"
    age = 56
    sex = "男"
    money = "56E"

    def make_money(self):
        print("马云很能赚钱")
        self.use_money()
    
    def use_money(self):
        print("挥金如土！")
    
d = Dada()
print(d.name)
d.make_money()

class Son(Dada):
    name = "小马"
    age = "18"

    def make_money(self,a1,a2):
        print("钱花光光")
        return a1 + a2
    def use_money(self):
        print("木有钱")
s = Son()
print(s.name)
b = s.make_money(2,5)
print(b)