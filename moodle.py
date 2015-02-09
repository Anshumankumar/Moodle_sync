#!/usr/bin/env python
# Author: Anshuman kumar

from moodleLogin import moodleLogin
from moodleFunction import *
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import os

url="http://moodle.iitb.ac.in"
opener = moodleLogin()

courseList = getCourseList(opener,url)
print (courseList)

""" 
for  in start:
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
"""
