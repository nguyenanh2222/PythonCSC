from xml.dom.minidom import parse
import xml.dom.minidom

DOMtree = xml.dom.minidom.parse("files_xml/student.xml")
collection = DOMtree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s" % collection.getAttribute("shelf"))

students = collection.getElementsByTagName("student")

for student in students:
    print("{:*^17}".format("Student"))
    if student.hasAttribute("id"):
        print("ID: %s" % student.getAttribute("id"))
    name = student.getElementsByTagName('name')[0]
    print("Name: %s" % name.childNodes[0].data)
    date = student.getElementsByTagName('date')[0]
    print("Date of birth: %s" % date.childNodes[0].data)