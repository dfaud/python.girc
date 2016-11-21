try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

url = "https://espace-personnel.agirc-arrco.fr/static/agirc-arrco/esaa/img/gps_btpr.jpg"
urlretrieve(url, "local-filename.jpg")
