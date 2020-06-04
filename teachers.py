import re

class Teachers(object):
    """docstring for Teachers."""

    def __init__(self):
        super(Teachers, self).__init__()

    def get_teachers(self,data):
        pattern ='Profesor:.+?\.'
        match = re.findall(pattern,data,flags=re.MULTILINE|re.UNICODE)
        match = "".join(match)
        pattern = ' .+?\.'
        match = re.findall(pattern,match,flags=re.MULTILINE|re.UNICODE)
        matches=[]
        for one_match in match:
            matches.append(re.sub('\.','',one_match,flags=re.MULTILINE|re.UNICODE))
        return(matches)

    def clean_teachers_data(self,all_data):
        raw_teachers=[]
        for data in all_data:
            teacher=self.get_teachers(data)
            if teacher:
                raw_teachers.append(teacher[0])
            else:
                raw_teachers.append("no value")
        print(list(set(raw_teachers)))
        return list(set(raw_teachers))

    def create_dict_teachers(self,data):
        array_teachers = []
        for teacher in data:
            dict = {}
            dict['name']=teacher
            dict['status']=1
            array_teachers.append(dict)
        return(array_teachers)
