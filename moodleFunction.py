# Author: Anshuman kumar
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
    linkInfo = coursePageB.find_all('li', 'modtype_resource')
    for i in range(0,len(linkInfo)):
        linkInfo[i] = linkInfo[i].find('a').get('href',None)
    return linkInfo

def saveFiles(filelist,dirname,openlink):
    for files in filelist:
        openfile = openlink.open(files)
        if  openfile.info()['Content-Type']!="text/html; charset=utf-8":
            current = openfile.info()['content-disposition'].split('=')[1].replace('"','')
            f = open(dirname +'/'+str(current), 'wb')
            f.write(openfile.read())
            f.close()
     
