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
for course in courseList.items():
    print(course[0])
    dirName='MyCourses/'+ str(course[0])
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    filelinks = getCourseContent(course[1],opener)
    saveFiles(filelinks,dirName,opener)
    
