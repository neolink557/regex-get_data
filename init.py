import teachers
import connection
import modify_data

m = modify_data.Data()
t = teachers.Teachers()
c = connection.Connection()
teachers_payload=[]
teachers_payload = t.create_dict_teachers(t.clean_teachers_data(m.find_data()))
for teacher in teachers_payload:
    c.post('teachers/', teacher)
