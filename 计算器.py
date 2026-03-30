num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
Operator = input("请输入运算符（+，-，*，/）：")
match Operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/" if num2 != 0 :
        print(num1 / num2)
    case _ :
        print("操作不支持")