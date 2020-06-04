import re
import teachers
import connection
import modify_data
import subjects

SUBJECT_PATTERN ='<tr role="row".*?</tr>'
TEACHER_PATTERN ='\(\d{1,2}\) Grupo.*?Cupos disponibles: \d'
TEACHER_FILENAME='teacher'
SUBJECT_FILENAME = 'subject'

ms = modify_data.Data(SUBJECT_FILENAME,SUBJECT_PATTERN)
mt = modify_data.Data(TEACHER_FILENAME, TEACHER_PATTERN)
t = teachers.Teachers()
s = subjects.Subjects()
c = connection.Connection()

print(t.create_dict_teachers(t.clean_teachers_data(mt.find_data())))
result = ms.find_data()
for subject in result:
    print(s.get_subjects(subject))
