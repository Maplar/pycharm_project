#函数的定义，函数定义的时候并不会执行
# def out_line():
#     print("********************")
#     print("--------------------")
# out_line()#调用函数
def circle_area(r):
    area = 3.14* r ** 2
    return area
print(circle_area(5))
def rectangle_area(l,w):
    area = l * w
    return area
print(rectangle_area(5,10))