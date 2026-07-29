#这里将会写一个简易的学生管理系统

class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名: {self.name}, 语文: {self.chinese}| 数学: {self.math}| 英语: {self.english}"

    def total_score(self):
        return self.chinese + self.math + self.english

    def update(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class EduManagementSystem:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)

    def update_student(self,name,chinese=None,math=None,english=None):
        for s in self.students:
            if s.name == name:
                s.update(chinese,math,english)
                return
        print(f"未找到学生: {name}")

    def delete_student(self,name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return
        print(f"未找到学生: {name}")

    def query_student(self,name):
        for s in self.students:
            if s.name == name:
                print(s)
                return
        print(f"未找到学生: {name}")

    def display_all_students(self):
        if len(self.students) == 0:
            print("没有学生信息。")
            return
        for s in self.students:
            print(s)

    def run(self):
        print("欢迎使用学生管理系统")
        while True:
            print("1.添加学生  2.修改学生信息  3.删除学生  4.查询学生  5.显示所有学生  6.退出")
            choice = input("请选择操作(1-6):")
            match choice:
                #添加学生
                case "1": 
                    name = input("请输入学生姓名：")
                    for s in self.students:
                        if s.name == name:
                            print("学生已存在，请勿重复添加。")
                            return
                    chinese = int(input("请输入语文成绩："))
                    math = int(input("请输入数学成绩："))
                    english = int(input("请输入英语成绩："))
                    if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                        student = Student(name, chinese, math, english)
                        self.add_student(student)
                    else:
                        print("成绩输入无效，请输入0-100之间的成绩。")

                #修改学生信息
                case "2":
                    name = input("请输入要修改的学生姓名：")
                    for s in self.students:
                        if s.name == name:
                            chinese = int(input("请输入新的语文成绩（留空表示不修改）："))
                            math = int(input("请输入新的数学成绩（留空表示不修改）："))
                            english = int(input("请输入新的英语成绩（留空表示不修改）："))
                            if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                                self.update_student(name,chinese,math,english)
                                return
                            else:
                                print("成绩输入无效，请输入0-100之间的成绩。")
                                return
                    print(f"未找到学生: {name}")

                #删除学生
                case "3":
                    name = input("请输入要删除的学生姓名：")
                    self.delete_student(name)

                case "4":
                    name = input("请输入要查询的学生姓名：")
                    self.query_student(name)

                case "5":
                    self.display_all_students()

                case "6":
                    print("退出系统。")
                    break
                case _:
                    print("无效的选择，请重新输入。")



if __name__ == "__main__":
    system = EduManagementSystem()
    system.run()