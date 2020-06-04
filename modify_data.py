import re

class Data(object):
    """docstring for Data."""
    NAME=''
    PATTERN=''

    def __init__(self,file_name,pattern):
        super(Data, self).__init__()
        self.NAME = file_name+".txt"
        self.PATTERN = pattern

    def delete_spaces(self):
        with open(self.NAME,encoding="utf8") as stream:
            contents = stream.read()
            x=re.sub('\n','.',contents,flags=re.MULTILINE|re.UNICODE)
            with open(self.NAME,"w+",encoding="utf8") as a:
                a.write(x)

    def find_data(self):
        self.delete_spaces()
        with open(self.NAME,encoding="utf8") as stream:
            contents=stream.read()
            match=re.findall(self.PATTERN,contents,flags=re.MULTILINE|re.UNICODE)
        return match
