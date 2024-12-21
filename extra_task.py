grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
print(students_list)
students_list.sort()
print(students_list)

Aaron_grades = [5, 3, 3, 5, 4]
Aaron_average = sum(Aaron_grades)/len(Aaron_grades)
print(Aaron_average)
Bilbo_grades = [2, 2, 2, 3]
Bilbo_average = sum(Bilbo_grades)/len(Bilbo_grades)
print(Bilbo_average)
Johnny_grades = [4, 5, 5, 2]
Johnny_average = sum(Johnny_grades)/len(Johnny_grades)
print(Johnny_average)
Khendrik_grades = [4, 4, 3]
Khendrik_average = sum(Khendrik_grades)/len(Khendrik_grades)
print(Khendrik_average)
Steve_grades = [5, 5, 5, 4, 5]
Steve_average = sum(Steve_grades)/len(Steve_grades)
print(Steve_average)

students_keys = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
students_grades = [4.0, 2.25, 4.0, 3.6666666666666665, 4.8]
students_dict = dict(zip(students_keys, students_grades))
print(students_dict)
