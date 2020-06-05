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
t = teachers.Teachers()#needs the ctrl+ a and ctrl+v of the page
s = subjects.Subjects()#needs the html of the page
c = connection.Connection()

teachers=t.create_dict_teachers(t.clean_teachers_data(mt.find_data()))
for teacher in teachers:
    c.post("teachers/", teacher)

result = ms.find_data()

for subject in result:
    match=s.get_subjects(subject)
    json =s.create_dict_subjects(match)
    c.post("subjects/", json)
