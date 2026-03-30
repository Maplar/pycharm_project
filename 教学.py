ok_account = 6
ok_password = 8
account = int(input("请输入你的账号:"))
password = int(input("请输入你的密码："))
if account == ok_account and password == ok_password:
    print("登录成功")
elif account == ok_account and password != ok_password:
    print("密码错误")
    print("登陆失败")
elif account != ok_account and password == ok_password:
    print("账号错误")
    print("登陆失败")
else:
    print("账号密码错误")
    print("登陆失败")
