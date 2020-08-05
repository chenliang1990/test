# a = 20
# b = 15
# if a>b:
#     print("a比b大")
# elif a == b:
#     print("a和b一样大")
# else:
#     print("a比b小")

# userInfo = {"username":"admin","password":"123456"}
# username = input("请输入用户名: ")
# password = input("请输入密码: ")
# if username == userInfo.get("username"):
#     if(password == userInfo.get("password")):
#         print("登录成功!")
#     else:
#         print("密码错误!")
# else:
#     print("账号不存在!")

userInfo = {}
username = input("请输入用户名: ")
password = input("请输入密码: ")
if len(username)>5:
    if len(password)>8:
        userInfo[username] = username
        userInfo[password] = password
        print("注册成功! ")
    else:
        print("输入密码没有超过8位!")
else:
    print("注册失败!账号不符合规范")


    
