groupmates = [
    {
        "name": "Stu",
        "surname": "dent1",
        "exams": ["firstExam", "secondExam", "thirdExam"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Stu",
        "surname": "dent2",
        "exams": ["firstExam", "secondExam", "thirdExam"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Stu",
        "surname": "dent3",
        "exams": ["firstExam", "secondExam", "thirdExam"],
        "marks": [5, 5, 5]
    },
      {
        "name": "Stu",
        "surname": "dent4",
        "exams": ["firstExam", "secondExam", "thirdExam"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Stu",
        "surname": "dent5",
        "exams": ["firstExam", "secondExam", "thirdExam"],
        "marks": [5, 4, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)

