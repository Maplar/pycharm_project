import random
random_number = random.randint(1,100)
while True:
   admin_Number = int(input("请输入您猜的数字："))
   if admin_Number < random_number:
        print("小了")
   elif admin_Number > random_number:
        print("大了")
   else:
        print("恭喜，猜对了")
        break
print("生成是数字是",random_number)

