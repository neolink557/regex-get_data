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

career_id=int(input("id"))

#teachers
teachers=t.create_dict_teachers(t.clean_teachers_data(mt.find_data()))
for teacher in teachers:
    response=c.post("teachers/", teacher)
    if not response.status_code in range(200,299):
        print("NO CREADO")

#subjects
result = ms.find_data()
size=len(c.get("subjects/"))
for subject in result:
    match=s.get_subjects(subject)
    json =s.create_dict_subjects(match)
    dict = {}
    size=size+1
    dict['subject'] = size;
    dict['career'] = 1;
    response=c.post("subjects/", json)
    if response.status_code in range(200,299):
        c.post('subjectsbycareer/', dict)
    else:
        print("NO CREADO")
