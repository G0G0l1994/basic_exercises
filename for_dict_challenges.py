# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_stud={}
for student in students: #можно ли тут одним циклом обойтись?
    count_stud.setdefault("".join(student.values()),students.count(student))
for name,count in count_stud.items():
    print(f"{name}: {count}") 
    
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_stud={}
for student in students:
    for student in students: 
        count_stud.setdefault("".join(student.values()),students.count(student))
for k,v in count_stud.items():
    if v==max(count_stud.values()):
        print(f"Самое частое имя среди учеников: {k}")
        break

    
# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for cl in school_students:
    count_stud = {}
    for student in cl:
        for student in cl: 
            count_stud.setdefault("".join(student.values()),cl.count(student))
    for k,v in count_stud.items():
        if v == max(count_stud.values()):
            print(f"Самое частое имя в {school_students.index(cl)+1} классе: {k}")
            break    
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for cl in school:
    male=0
    female=0
    for name in cl['students']: 
        if is_male["".join(name.values())] == True:
            male+=1
        else:
            female+=1
    print(f"Класс {cl['class']}: девочки {female}, мальчики {male}")
    
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
max_male=0
max_female=0
for cl in school:
    male=0
    female=0
    for name in cl['students']: 
        if is_male["".join(name.values())] == True:
            male+=1
        else:
            female+=1
    if max_male < male:
        max_male = male
    if max_female < female:
        max_female = female
    cl.setdefault('male',male)
    cl.setdefault('female',female)
for cl in school:
    if cl['female'] == max_female:
        print(f"Больше всего девочек в классе {cl['class']}")
    if cl['male'] == max_male:
        print(f"Больше всего мальчиков в классе {cl['class']}")

