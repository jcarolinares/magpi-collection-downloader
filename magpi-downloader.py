from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys

#Creating the download folder
newpath ="./magpi-issues"
if not os.path.exists(newpath): os.makedirs(newpath)

#Looking the last published issue
r  = requests.get('https://www.raspberrypi.org/magpi/')
data = r.text
soup = BeautifulSoup(data,"lxml")
last_issue=soup.find('a',class_="btn mob-butt pdf-butt")
last_issue=str(last_issue)
last_issue=last_issue[last_issue.find("MagPi")+5:last_issue.find(">")-5]


print("\nLast issue number: {}".format(last_issue))

for issue in range(int(last_issue)):
    try:
        issue=issue+1
        if not os.path.exists("./magpi-issues/Magpi{:02d}.pdf".format(issue)):
            print("Downloading https://www.raspberrypi.org/magpi-issues/MagPi{:02d}.pdf".format(issue))
            urllib.urlretrieve ("https://www.raspberrypi.org/magpi-issues/MagPi{:2d}.pdf".format(issue), "./magpi-issues/Magpi{:02d}.pdf".format(issue))
    except():
        print(" \nERROR: There was an error downloading Magpi{:02d}\n".format(issue))
    else:
        print(" MagPi{:02d} Downloaded!\n".format(issue))


'''
#HTML references
<a href="https://www.raspberrypi.org/magpi-issues/MagPi63.pdf" class="btn mob-butt pdf-butt">Download pdf</a>
https://www.raspberrypi.org/magpi/
'''
