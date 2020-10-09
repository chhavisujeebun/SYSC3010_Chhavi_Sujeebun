
from urllib.parse import urlencode 
import time
import http.client as http
from urllib.request import urlopen

key = "7481QW0APO2BO2BU"
ProjectGroup= "L1-F-1"
Identifier="b"
cmailaddress="chhavisujeebun@cmail.carleton.ca"

URL='http://api.thingspeak.com/update?api_key='
HEADER='&field1={}&field2{}&field3{}'.format(ProjectGroup,Identifier,cmailaddress)
new_url=URL+key+HEADER
print(new_url)
update= urlopen(new_url)
print(update)