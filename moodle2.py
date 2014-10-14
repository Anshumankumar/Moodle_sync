import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import os

username = 'anshumankumar'
password = '14122012+'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open('http://moodle.iitb.ac.in/login/index.php', login_data)
resp = opener.open('http://moodle.iitb.ac.in/course/view.php?id=4233')
#print resp.read()

second=BeautifulSoup(resp)
Cname= str(second.title.string)
if not os.path.exists(Cname):
	    os.makedirs(Cname)
	    print "Making Directory..."
abc=second.find(id="region-main")
print str(abc.get('id'))
mainbulk=BeautifulSoup(str(abc))
abc=mainbulk.find_all('a')
for tag in abc:
	    files=tag.get('href')
	    current=str(tag.get_text())
	    if 'http://moodle.iitb.ac.in' in str(files):
			response=opener.open(files)
		    	print files;

		    	if  response.info()['Content-Type']!="text/html; charset=utf-8":
				f = open(Cname+'/'+str(current)+'.pptx', 'wb')
				f.write(response.read())
				f.close()

