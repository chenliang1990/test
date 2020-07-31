# a = input("请输入数字，逗号分割")
# b = a.split(",")
# print(len(b))
# c = int(b[0])
# d = int(b[1])
# print(c * d)
#字符串拼接数字
# d = []
# a = int(input("请输入第一个数: "))
# b = int(input("请输入第二个数: "))
# c = int(input("请输入第三个数: "))
# d.append(a)
# d.append(b)
# d.append(c)
# print("三个数字之和:{}".format(a+b+c))

e = [2,45,12,65,1231,0]
p = e.index(65)
print(p)
e.sort(reverse = True)
print(e)