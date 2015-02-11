# Author: Anshuman kumar
# Name: moodleFunction.py
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>


import urllib, urllib2, cookielib
from bs4 import BeautifulSoup

def getCourseList(openlink,url):
    """
        This function takes the login instance of moodle and get all
        the course name and link
        @input open moodle link instance , url of moodle website
        @output The dictionary consisting of course name and its instance. 
    """
    courseList = {}
    mainPage = openlink.open(url)
    mainPageB = BeautifulSoup(mainPage)
    courseDataList = mainPageB.find_all('h3','coursename')
    for courseData in courseDataList:
        linktoCoursePage = courseData.find('a').get('href',None)
        courseName =  str(courseData.find('a').contents[0])
        courseList[courseName] = linktoCoursePage
    return courseList

def getCourseContent(courselink,openlink):
    coursePage = openlink.open(courselink)
    coursePageB = BeautifulSoup(coursePage)
    coursePageB = coursePageB.find('div', 'course-content')
    forumInfo =  coursePageB.find('li', 'modtype_forum') 
    forumLink = forumInfo.find('a').get('href',None)
    forumPage = BeautifulSoup(openlink.open(forumLink))
    linkForum = forumPage.find_all('td', 'topic')
    linkInfo = coursePageB.find_all('li', 'modtype_resource')
    for i in range(0,len(linkInfo)):
        linkInfo[i] = linkInfo[i].find('a').get('href',None)
    for i in range(0,len(linkForum)):
        linkForum[i] = linkForum[i].find('a').get('href',None)
        topicPage = BeautifulSoup(openlink.open(linkForum[i]))
        attacInfo = topicPage.find_all('div', 'attachments')
        for attac in attacInfo:
            attac = attac.find('a').get('href',None)
            linkInfo.append(attac)
    return linkInfo

def saveFiles(filelist,dirname,openlink):
    for files in filelist:
        openfile = openlink.open(files)
        if  openfile.info()['Content-Type']!="text/html; charset=utf-8":
            current = openfile.info()['content-disposition'].split('=')[1].replace('"','')
            f = open(dirname +'/'+str(current), 'wb')
            f.write(openfile.read())
            f.close()
     
