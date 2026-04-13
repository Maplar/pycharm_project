Student_Information = {}
menu = """
############  学生教务管理系统  ##########
#         1.添加学生信息                # 
#         2.修改学生信息                #
#         3.删除学生信息                #
#         4.查询学生信息                #
#         5.列出所有学生信息             # 
#         6.统计班级语文,数学,           #
#         英文成绩的最高分,最低分,        # 
#         平均分,以及语文,数学,          #
#         英文最高分和最低分的学生姓名     # 
#         7.退出系统                   #
#######################################
"""
print("欢迎使用学生教务管理系统~")
while True:
    print(menu)
    choice = int(input("请输入您的选择（1-7）："))
    match choice:
        case 1:
            student_name = input("请输入要添加的学生姓名：")
            student_chinese = float(input("请输入要添加的学生语文成绩："))
            student_math = float(input("请输入要添加的学生数学成绩："))
            student_english = float(input("请输入要添加的学生英语成绩："))
            if student_name in Student_Information:
                print("该学生已存在，请重新选择 ~")
            else:
                Student_Information[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
                print("学生信息添加完毕 ~")
        case 2:
            student_name = input("请输入要修改的学生姓名：")
            if student_name not in Student_Information:
                print("该学生不存在，请重新选择 ~")
                continue
            student_chinese = float(input("请输入要修改的学生语文成绩："))
            student_math = float(input("请输入要修改的学生数学成绩："))
            student_english = float(input("请输入要修改的学生英语成绩："))
            Student_Information[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
            print("学生信息修改完毕 ~")
        case 3:
            student_name = input("请输入要删除的学生姓名：")
            if student_name not in Student_Information:
                print("该学生不存在，请重新选择 ~")
            else:
                del Student_Information[student_name]
                print("学生信息删除完毕 ~")
        case 4:
            student_name = input("请输入要查询的学生姓名：")
            if student_name not in Student_Information:
                print("该学生不存在，请重新选择 ~")
            else:
                print(f"{student_name} - 语文成绩：{Student_Information[student_name]['chinese']}，数学成绩：{Student_Information[student_name]['math']}，英语成绩：{Student_Information[student_name]['english']}")
        case 5:
            if not Student_Information:
                print("没有任何学生信息 ~")
            else:
                print("所有学生的信息如下：")
                for student_name, student_info in Student_Information.items():
                    print(f"{student_name} - 语文成绩：{student_info['chinese']}，数学成绩：{student_info['math']}，英语成绩：{student_info['english']}")
        case 6:
            top_chinese = max(Student_Information.items(), key=lambda x: x[1]['chinese'])
            top_math = max(Student_Information.items(), key=lambda x: x[1]['math'])
            top_english = max(Student_Information.items(), key=lambda x: x[1]['english'])
            low_chinese = min(Student_Information.items(), key=lambda x: x[1]['chinese'])
            low_math = min(Student_Information.items(), key=lambda x: x[1]['math'])
            low_english = min(Student_Information.items(), key=lambda x: x[1]['english'])
            avg_chinese = sum(student_info['chinese'] for student_info in Student_Information.values()) / len(Student_Information)
            avg_math = sum(student_info['math'] for student_info in Student_Information.values()) / len(Student_Information)
            avg_english = sum(student_info['english'] for student_info in Student_Information.values()) / len(Student_Information)
            print(f"语文成绩最高分：{top_chinese[1]['chinese']}，学生姓名：{top_chinese[0]}；最低分：{low_chinese[1]['chinese']}，学生姓名：{low_chinese[0]}；平均分：{avg_chinese}")
            print(f"数学成绩最高分：{top_math[1]['math']}，学生姓名：{top_math[0]}；最低分：{low_math[1]['math']}，学生姓名：{low_math[0]}；平均分：{avg_math}")
            print(f"英语成绩最高分：{top_english[1]['english']}，学生姓名：{top_english[0]}；最低分：{low_english[1]['english']}，学生姓名：{low_english[0]}；平均分：{avg_english}")
        case 7:
            print("感谢使用学生教务管理系统，再见！")
            break
        case _:
            print("输入有误，请重新输入！")




