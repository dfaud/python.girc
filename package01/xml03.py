from xml.dom import minidom
dom = minidom.parse('fic.xml')
conference=dom.getElementsByTagName('conference')
for node in conference:
    conf_name=node.getAttribute('name')
    print conf_name
    alist=node.getElementsByTagName('author')
    for a in alist:
# authortext= a.nodeValue
        authortext= a.childNodes[0].nodeValue
        print authortext
