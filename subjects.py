import re

class Subjects(object):
    """docstring for Teachers."""

    def __init__(self):
        super(Subjects, self).__init__()

    def get_subjects(self,data):
        pattern ='<span .*?</span>'
        match = re.findall(pattern,data,flags=re.MULTILINE|re.UNICODE)
        print(match)
        match = "".join(match)
        return(match)
