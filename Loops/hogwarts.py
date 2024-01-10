# students = ["Hermoi", "Harry", "ROn"]

# # print(students[0]) # you print certain value at certain index

# # for student in students:
# #     print(student)
    
# # how can yo know the range of list

# for i in range(len(students)):
#     print(i, students[i])


# Dict


# lets create a dictonary
students = {
    "Hermoi":"home1",
    "Harry":"home1",
    "Ron":"home3",
    "rex":"home5",
    }
print(students["Hermoi"]) # in dictonary yo need to use the word as identifier

for stu in students:
    # print(stu) # This will give you keys
    print(stu, students[stu])