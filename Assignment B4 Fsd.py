'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
student_1 ={}

student_2 ={}

student_3 ={}


Main_D = [
    student_1,
    student_2,
    student_3,
]
for i in range (len(Main_D)):
    name = input("Enter student name, press q for quit: ")
    if name == "q":
        break
    else:
        Main_D[i]["name"] = name
        age = int(input("Enter age: "))
        Main_D[i]["age"] = age
        work = input("Enter work: ")
        Main_D[i]["work"] = work
        skills = []
        skills.append(input("Enter skills: "))
        skills.append(input("Enter skills: "))
        skills.append(input("Enter skills: "))
        Main_D[i]["skills"] = skills
        degree= {}
        degree["title"] = input("Enter degree title: ")
        degree["major"] = input("Enter degree major: ")
        degree["completiondate"] = input("Enter degree completiondate: ")
        Main_D[i]["degree"] = degree
        salary = int(input("Enter salary: "))
        Main_D[i]["salary"] = salary

print(Main_D)

