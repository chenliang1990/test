# 构造方法的使用

class Bird():
    name = ""
    age = 0
    sex = ""

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s

b = Bird("小红",20,"女")
b.name = "小花"
print(b.name,b.age,b.sex)

