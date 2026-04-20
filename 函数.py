#函数的定义，函数定义的时候并不会执行
# def out_line():
#     print("********************")
#     print("--------------------")
# out_line()#调用函数
# def circle_area(r):
#     area = 3.14* r ** 2
#     return area
# print(circle_area(5))
# def rectangle_area(l,w):
#     area = l * w
#     return area
# print(rectangle_area(5,10))



# def calc_score(socre_list):
#     max_s = max(socre_list)
#     min_s = min(socre_list)
#     avg_s = round(sum(socre_list) / len(socre_list),1)
#     return max_s , min_s , avg_s
# s_list = [567,345,765,789,543,458]
# max_socre, min_socre, avg_socre = calc_score(s_list)
# print(max_socre, min_socre, avg_socre)

#def X(s):

# def X(*args):
#     min_x = min(args)
#     max_x = max(args)
#     avg_x = sum(args) / len(args)
#     return min_x, max_x, round(avg_x, 1)
# args = input("请输入一组数字，以逗号分隔：")
# args_list = args.split(',')
# num_list = [int(X) for X in args_list]
# print(num_list)
# num_list = X(*num_list)
# print(num_list)