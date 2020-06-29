import xml.sax
from doc import Doc


class DocHandler( xml.sax.ContentHandler ):
    def __init__(self, es):
        self.CurrentData = ""
        self.doc = Doc()
        self.title = ""
        self.abstract = ""
        self.index = 0
	self.es = es
        
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        #print(tag)
        if tag == "doc":
            self.index = self.index + 1
            print("Doc: ", self.index)
            #print([s.toString() for s in docs])
            
    def endElement(self, tag):
        #print(tag)
        if tag == "doc":
            self.es.index(index='temp1', doc_type='wikiabstract', id=self.index, body=json.loads(self.doc.toString()))
        elif self.CurrentData == "title":
            self.doc.title = self.title
        elif self.CurrentData == "abstract":
            self.doc.abstract = self.abstract

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "abstract":
            self.abstract = content
            #print(content)
