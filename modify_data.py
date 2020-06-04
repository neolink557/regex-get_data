import re

class Data(object):
    """docstring for Data."""
    NAME='horario.txt'

    def __init__(self):
        super(Data, self).__init__()

    def delete_spaces(self):
        with open(self.NAME,encoding="utf8") as stream:
            contents = stream.read()
            x=re.sub('\n','.',contents,flags=re.MULTILINE|re.UNICODE)
            with open(self.NAME,"w+",encoding="utf8") as a:
                a.write(x)

    def find_data(self):
        self.delete_spaces()
        pattern ='\(\d\) Grupo.*?Cupos disponibles: \d'
        with open(self.NAME,encoding="utf8") as stream:
            contents=stream.read()
            match=re.findall(pattern,contents,flags=re.MULTILINE|re.UNICODE)
        return match
