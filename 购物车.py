shopping_cart = {}
menu = """
######## 购物车系统 ########
#       1.添加购物车       #
#       2.修改购物车       #
#       3.删除购物车       #
#       4.查询购物车       #
#       5.退出购物车       #
##########################
"""
print("欢迎使用购物车管理系统~")
while True:
    print(menu)
    choice = int(input("请输入您的选择（1-5）："))
    match choice:
        case 1:
            goods_name = input("请输入要添加的商品名称：")
            goods_price = float(input("请输入要添加的商品价格："))
            goods_num = int(input("请输入要添加的商品数量："))

            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择 ~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕 ~")
        case 2:
            goods_name = input("请输入要修改的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择 ~")
                continue
            goods_price = float(input("请输入要修改的商品价格："))
            goods_num = int(input("请输入要修改的商品数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完毕 ~")
        case 3:
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择 ~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕 ~")
        case 4:
            if not shopping_cart:
                print("购物车为空 ~")
            else:
                print("购物车中的商品如下：")
                for goods_name, goods_info in shopping_cart.items():
                    print(f"{goods_name} - 价格：{goods_info['price']} 元，数量：{goods_info['num']} 件")
        case 5:
            print("感谢使用购物车管理系统，再见！")
            break
        case _:
            print("输入有误，请重新输入！")
