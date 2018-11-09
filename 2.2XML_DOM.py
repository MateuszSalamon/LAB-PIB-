from xml.dom import minidom
import sys

# Open XML
DOMTree = minidom.parse('plik.xml')
DOMTree.getElementsByTagName("imie")[0].childNodes[0].nodeValue = "Zbychu"

# get elements of XML
cNodes = DOMTree.childNodes

#DOMTree.getElementsByTagName("osoba")[0].childNodes[0].nodeValue = "Zbychu"

a =DOMTree.writexml(sys.stdout, addindent=" ",newl="\n")

for i in cNodes[0].getElementsByTagName("osoba"):
	# nazwa taga
	print(i.getElementsByTagName("imie")[0].nodeName)
	# wartosc taga
	print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
	# dostep do atrybutu
	print(i.getElementsByTagName("imie")[0].getAttribute("foo"))

