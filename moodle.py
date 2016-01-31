#!/usr/bin/env python2

# Author: Anshuman kumar
# Name: moodle.py
# It syncs all the file from your moodle to a directory in your computer

#    Copyright (C)  2014 Anshuman kumar

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from moodleLogin import moodleLogin
from moodleFunction import *
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import easygui as eg
import os
import pickle

url="http://moodle.iitb.ac.in"
opener = moodleLogin()

courseList = getCourseList(opener,url)
try:
    f = open('course','r')
    choice = f.read().splitlines()
except IOError:
    choice =eg.multchoicebox("Courses to Sync","MoodleSync",courseList.keys())
    f = open('course','w')
    f.write("\n".join(choice))
    f.close()


cList ={}
for course in choice:
    cList[course] = courseList[course]


for course in cList.items():
    print(course[0])
    dirName='MyCourses/'+ str(course[0])
    openHistory(dirName)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    filelinks = getCourseContent(course[1],opener)
    saveFiles(filelinks,dirName,opener)
    saveHistory(dirName)

