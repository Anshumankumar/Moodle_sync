import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import os

username = 'anshumankumar'
password = '14122012+'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open('http://moodle.iitb.ac.in/login/index.php', login_data)
resp = opener.open('http://moodle.iitb.ac.in')
#print resp.read()
url="http://moodle.iitb.ac.in"
page=BeautifulSoup(resp)
start=page.find_all(title="Click to enter this course")
for tag in start:
    link = tag.get('href',None)
    if link != None:
    	new=opener.open(link)
	second=BeautifulSoup(new)
	Cname='MyCourses/'+ str(second.title.string)
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
	        nextpage=BeautifulSoup(response)
	        bbb=nextpage.find(id="region-main")
	        mainbulk2=BeautifulSoup(str(bbb))
	        abc2=mainbulk2.find_all('a')
	        for tag in abc2 :
	      	    files2=tag.get('href')
	    	if files2 != None	and  'http://moodle.iitb.ac.in/pluginfile.php' in str(files2):
		    response2=opener.open(files2)
		    print files2
		    if  response2.info()['Content-Type']!="text/html; charset=utf-8":
			f = open(Cname+'/'+str(current), 'wb')
			f.write(response2.read())
			f.close()

