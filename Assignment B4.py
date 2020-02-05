Main_D = [
    student_1 {},
    student_2 {},
    student_3 {},
]

for i in range (3):
    Main_D[i][id] = i
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
            skills[0]= input("Enter skills: ")
            skills[1]= input("Enter skills: ")
            skills[2]= input("Enter skills: ")
            Main_D[i]["skills"] = skills

print(Main_D)