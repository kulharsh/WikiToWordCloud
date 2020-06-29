import json

class Doc() :
    def __init__(self):
        self.title = ""
        self.abstract = ""
    def toString(self):
        return json.dumps(self.__dict__)
