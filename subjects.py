import re
import unicodedata

class Subjects(object):
    """docstring for Teachers."""

    def __init__(self):
        super(Subjects, self).__init__()

    def get_subjects(self,data):
        pattern ='<span .*?</span>'
        match = re.findall(pattern,data,flags=re.MULTILINE|re.UNICODE)
        matches=[]
        for subject in match:
            matches.append(self.clean_subjects_data(subject))
        return(matches)

    def get_code(self,data):
        pattern ='tabindex="0">.*</a>'
        match = re.findall(pattern,data,flags=re.MULTILINE|re.UNICODE)
        match=re.sub('tabindex="0">','',match[0],flags=re.MULTILINE|re.UNICODE)
        match=re.sub('<','',match[0],flags=re.MULTILINE|re.UNICODE)
        return(match)

    def clean_subjects_data(self,data):
        pattern ='title="">.*?<'
        match = re.findall(pattern,data,flags=re.MULTILINE|re.UNICODE)
        matches=[]
        for one_match in match:
            matches.append(re.sub('title="">','',one_match,flags=re.MULTILINE|re.UNICODE))
        match = matches.copy()
        matches.clear()
        for one_match in match:
            matches.append(re.sub('<','',one_match,flags=re.MULTILINE|re.UNICODE))
        return(matches)

    def create_dict_subjects(self,data):
        dict = {}
        typology=0
        dict['name']=data[1][0]
        dict['credits_number']=data[2][0]
        str=unicodedata.normalize("NFKD", data[3][0]).upper().lower()
        str=re.sub(' \(.*\)','',str,flags=re.MULTILINE|re.UNICODE)
        if str == "disciplinar obligatoria":
            typology = 1
        elif(str == "fund. obligatoria"):
            typology = 2
        elif(str == "disciplinar optativa"):
            typology = 3
        elif(str == "fund. optativa"):
            typology = 4
        elif(str == "nivelación"):
            typology = 5
        else:
            typology =1

        dict['typology']=typology
        return(dict)
