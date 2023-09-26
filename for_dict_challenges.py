from collections import Counter
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
count_stud = {}
names = [student['first_name'] for student in students]
ctr = Counter(names)
for name,count in ctr.items():
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
    if student['first_name'] not in count_stud:
        count_stud[student['first_name']] = 1
    else:
        count_stud[student['first_name']] += 1
print(f"Самое частое имя среди учеников: {max(count_stud.keys(),key = count_stud.get)}")


    
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
    male = [name['first_name'] for name in cl['students'] if  is_male[name['first_name']]]
    female = [name['first_name'] for name in cl['students'] if not is_male[name['first_name']]]
    print(f"Класс {cl['class']}: девочки {len(female)}, мальчики {len(male)}")
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


for cl in school:
    male = [name['first_name'] for name in cl['students'] if is_male[name['first_name']]]
    female = [name['first_name'] for name in cl['students'] if not is_male[name['first_name']]]
    if len(male) > len(female):
        print(f"Больше всего мальчиков в {cl['class']}")
    else:
        print(f"Больше всего девочек в {cl['class']}")