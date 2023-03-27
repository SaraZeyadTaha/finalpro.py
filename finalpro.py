import random


class Course:
    def __init__(self, course_id, course_name, course_level):
        self.course_id = course_id
        self.course_name = course_name
        self.course_level = course_level

    def get_course(self):
        return self.__dict__



class Student:
    def __init__(self, name, number, level):
        self.__student_name = name
        self.__student_number = number
        self.__student_level = level
        self.__student_course = []

    def get_name(self):
        return self.__student_name

    def get_number(self):
        return self.__student_number

    def get_level(self):
        return self.__student_level

    def get_course(self):
        return self.__student_course

    def set_name(self, new_name):
        self.__student_name = new_name

    def set_level(self, new_level):
        self.__student_level = new_level

    def add_course(self, course):
        if student_list[i].get_level() in course.course_level:
            student_list[i].get_course().append(course.course_name)
            #self.__student_course.append(course.course_name)
            print(" Done ")
        else:
            print("student_class as same as course_class")

    def student_details(self):
        return self.__student_name + self.__student_level + self.__student_course





x = 1
student_list = []
course_list = []
while x == 1:
    print("1. Add new student ")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display all Student ")
    print("5. Create new course")
    print("6. Add course to student")
    print("7. Exit")
    choice = int(input("Select Choice Please"))

    if choice == 1:
        nname = input("enter student name: ")
        while True:
            test = input("select level(A-B-C): ")
            if test == "a" or test == "A" or test == "b" or test == "B" or test == "c" or test == "C":
                llevel = test
                break
        number_stu = input("enter student number")
        student_list.append(Student(name=nname, number=number_stu, level=llevel))
        print("student saved successfully")

    if choice == 2:
        number_remove = input("enter number of student want to remove : ")
        z = 0
        for i in range(len(student_list)):
            if number_remove in student_list[i].get_number():
                student_list.remove(student_list[i])
                print("done")
                z = z+1
                break
        if z == 0:
            print("user not exist")

    if choice == 3:
        edit = input("enter number of student want to edit:")
        for i in range(len(student_list)):
            if edit in student_list[i].get_number():
                new_name = input(" enter new name")
                student_list[i].set_name(new_name)

                while True:
                    new_llevel = input(" select new level (A,B,C)")
                    if new_llevel == "a" or new_llevel == "A" or new_llevel == "b" or new_llevel == "B" or new_llevel == "c" or new_llevel == "C":
                        student_list[i].set_level(new_level=new_llevel)
                        print("done")
                        break

    if choice == 4:

        print("All Student :")
        for i in range(len(student_list)):
            print(" name : " + " " + student_list[i].get_name() + "   " + " level : " + "  " + student_list[i].get_level()+"  courses: ")
            print(student_list[i].get_course())

    if choice == 5:
        name_cl = input("enter class name :")
        id = input("enter course id: ")
        while True:
            level = input("select course_level (A-B-C)")
            if level == "a" or level == "A" or level == "b" or level == "B" or level == "c" or level == "C":
                level_co = level
                break
        course_list.append(Course(course_name=name_cl, course_id=id, course_level=level))
        print("course saved successfully")

    if choice == 6:
        v = 1
        num = input("enter student number want to add course")
        for i in range(len(student_list)):
            if num in student_list[i].get_number():
                id = input("enter course id: ")
                for j in range(len(course_list)):
                    if id == course_list[j].course_id:
                        student_list[i].add_course(course=course_list[j])
                        v = 0
                        print("done")

        if v == 1:
            print("course not exist")

    if choice == 7:
        x = 0
        exit()









































