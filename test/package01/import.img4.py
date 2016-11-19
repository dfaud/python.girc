import urllib
resource = urllib.urlopen("https://espace-personnel.agirc-arrco.fr/static/agirc-arrco/esaa/img/gps_btpr.jpg")
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()
