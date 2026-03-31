while True:
    username = input("请输入正确的用户名：")
    password = input("请输入正确的用密码：")

    if username == "" or password == "":
        print("输入的用户名或者密码为空，请重新输入。")

    if username == "admin" and password == "666888":
        print("登陆成功")
        break
    else:
        print("用户名或者密码错误，请重新输入。")

