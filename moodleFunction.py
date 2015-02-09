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

