import xml.sax


class StudentHandler(xml.sax.ContentHandler):
    sl = 0
    def __int__(self):
        self.CurrentData = ""
        self.phone = ""
        self.name = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        print("List of contacts: ")

        if tag == "contact":
            print("--- Contact ", StudentHandler.sl, "---")
            name = attributes["name"]
            print("Name: ", name)
            phone = attributes["phone"]
            print("Phone: ", phone)
        StudentHandler.sl += 1
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Hanler = StudentHandler()
    parser.setContentHandler(Hanler)
    parser.parse("files_xml/contact.xml")
