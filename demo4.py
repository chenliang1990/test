# list = ["zhang","chen","wang"]
# password = input("请输入三个密码用，隔开:")
# pwd = password.split(",")
# student = {list[0]:pwd[0],list[1]:pwd[1],list[2]:pwd[2]}
# print(student)


"""
元组只有index(),count()两个方法
数组有del()删除下标,remove()删除具体某个值,pop(4)取走,index(),count()
append(),insert(),extend(),sort(reverse=True),clear()这些方法
字典有get(),update(),pop(),keys(),values(),items(),del a["name"]删除
"""
# a = {"name":"张三","age":30,"address":"厦门","girlfiend":["小红","小黑","婷婷","梅梅"],
# "brother":("小刚","小王")}
# print(a.pop("name"))
# a.update(sex = "男")
# print(a)
# print(a.get("brother"))
# a["sex"] = "女"
# print(a)
# print(list(a.keys()))
# print(list(a.values()))
# print(list(a.items()))

a = eval("(1,'你好',True)")
print(type(a))