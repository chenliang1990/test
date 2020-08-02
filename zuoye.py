
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end = "  ")
#     print()

# a = "你好，我肚子额了"
# for i in a:
#     print(i)

# a = 1
# while a < 5:
#     print("今天真困!")
#     a = a + 1

# # sum = 0
# # for i in range(1,101):
# #     sum = sum+i
# # print(sum)

# sum = 0
# i = 1
# while i < 101:
#     sum = sum + i
#     i = i + 1
# print(sum)


# 7、现在有一堆成绩，请把及格的和不及格的分别放到不同的数组中。
# [{"tom":98,"king":56,"lili":75}]
high = {}
low = {}
chenji = {"tom":98,"king":56,"lili":75,"chen":50}
for i in chenji:
    if chenji.get(i) >= 60:
        high[i] = chenji.get(i)
    else:
        low[i] = chenji.get(i)

print(high)
print(low)
# 8、使用python的print，模拟一个红绿灯的功能,红灯30秒，绿灯35秒，黄灯3秒。
light = {"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light.get(i)):
        print(i,"还剩",light.get(i)-j,"秒")

# 9、实现一个注册功能，要求账号5-8位，并且小写字母开头，不允许符号，仅小写字母和数字组成。
# 密码8-12位，并且密码必须包含3种字符串，比如aaa123!。
username = input("请输入账号: ")
password = input("请输入密码: ")
if len(username) >= 5 and len(username) <= 8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >= 8 and len(password) <= 12:
            print("注册成功",{username:password})
        else:
            print("输入的密码长度不对")
    else:
        print("账号的首字母必须为小写")

else:
    print("输入的账号长度不符合规范")

