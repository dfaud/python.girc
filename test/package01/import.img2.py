import urllib
import StringIO
import Image
 
                                    page =urllib.urlopen("https://espace-personnel.agirc-arrco.fr/static/agirc-arrco/esaa/img/gps_btpr.jpg")
                                    buffer = page.read()
                                    im = Image.open(StringIO.StringIO(buffer))
                                    im.save	("test.jpg")
