#用户注册
from dbtools import query,commit

# username = input("请输入用户名: ")
# password = input("请输入密码: ")

# sql = 'insert into t_pymysql_account values(null,"{}","{}")'.format(username,password)
# print(sql)
# commit(sql)

#用户登录
username = input("请输入用户名: ")
password = input("请输入密码: ")

sql = "select * from t_pymysql_account where username = '{}' and password = '{}'".format(username,password)
r = query(sql)
print(r)
if len(r) == 0:
    print("登录失败")
else:
    print("登录成功")