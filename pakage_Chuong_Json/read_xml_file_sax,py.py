import xml.sax
class StudentHandler(xml.sax.ContentHandler):
    def __int__(self):
        self.CurrenData = ""
        self.ids = ""
        self.name = ""
        self.date = ""
    def startElemnet(self, tag, arrtibuttes):
        self.CurrenData = tag
        if tag == "student":
            print(":*^5".format('Student'))
            ids = arrtibuttes["id"]
            print("ID: ", ids)

    def endElemnet(self, tag):
        if self.CurrenData == "id"
            print("ID: ", self.ids)
        elif self.CurrenData == "name":
            print("name: ", self.name)
        elif self.CurrenData == "date":
            print("date: ", self.date)
        self.CurrenData = ""

    def characters(self, content):
        if self.CurrenData =="id":
            self.ids = content
        elif self.CurrenData == "name":
            self.name = content
        elif self.CurrenData == "date":
            self.date = content

if __name__=="__main__":
    parser = xml.sax.make_parser()
    parser.setContentHandler(xml.handler.feature_namespaces, 0)
    Handler = StudentHandler()
    parser.setContentHandler(Handler)
    parser.parse("student.xml")

