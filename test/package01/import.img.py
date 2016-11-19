import urllib2
 
#on chope la source
im = urllib2.urlopen('https://espace-personnel.agirc-arrco.fr/static/agirc-arrco/esaa/img/gps_btpr.jpg')
source = im.read()
 
#on cree le fichier
file('gps_btpr.jpg', 'wb')
 
#on transfert le tout dans le fichier
fichier = open('gps_btpr.jpg', 'wb')
fichier.write(source)
fichier.close()
