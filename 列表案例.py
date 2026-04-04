num_list = []
for i in range(10):
    num = int(input(f"请输入{i+1}个数字："))
    num_list.append(num)
print("数字列表",num_list)
num_list.sort()
print(num_list)
print("最小值：",num_list[0])
print("最大值：",num_list[-1])
print("平均值：",sum(num_list)/len(num_list))