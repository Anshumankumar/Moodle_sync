# Author: Anshuman kumar
# Name: moodleLogin.py
# It login to your moodle account

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
 

