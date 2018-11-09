import xml.sax


class ABContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("startElement '" + name + "'")
        if name == "imie":
            print("id = " + attrs.getValue("foo"))

    def endElement(self, name):
        print("endElement " + name)

    def characters(self, content):
        if content != "\n":
            print("characters " + content)


def main(source_file_name):
    source = open(source_file_name)
    xml.sax.parse(source, ABContentHandler())



if __name__ == "__main__":
    main("plik2.xml")
