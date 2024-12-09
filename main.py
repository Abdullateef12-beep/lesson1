fruits = ["apple" ,"banana," ,"cherry"]

name_age = {
    "nistha" :30,
    "abdulla" :12
}


subjects_marks = {
    "maths" :55,
    "english" : 50,
    "computer science" :30,
    "science" :55,
    "PE" :15, 

}

print(subjects_marks)

students_marks = {
    "abdullateef" : 99,
    "nishtha" :80,
    "anna" :98,
    "anas" :95

}

print("marks of nishtha are :" , students_marks["nishtha"])


students_marks["Abdullateef"] = 100
print(students_marks)


students_marks["nishtha"] = 90
print(students_marks)

students_marks["sam"] = 85
print(students_marks)

del students_marks["nishtha"]
print(students_marks) 

if "nishtha" in students_marks:
   print("Nishtha is part of the class")
else:
    print("nishtha is not part of the given class." )