from userInput import userInput
import urllib, urllib2, cookielib
def moodleLogin():
    """ This function login to moodle.iitb.ac.in
        @input: None
        @output: instance of login page of moodle
    """ 
    userInfo = userInput();
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode(userInfo);
    opener.open('http://moodle.iitb.ac.in/login/index.php', login_data)
    return opener 
 

