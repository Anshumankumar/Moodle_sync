#TODO  Make a gui interface for taking the input
#TODO  Make the a secure way to save username and password


import os.path
import ast

def userInput():
    """
        This function take the user name and password and return
        If a particular file exist it would seach for file and update info
        @input: NONE
        @output: dictiary consisting of user name and password
    """
    
    if os.path.isfile('info'):
        f = open('info','r')
        userInfo = ast.literal_eval(f.read())
        f.close()
    else:    
        username = str(raw_input('Enter your Username: '))
        password = str(raw_input('Enter Your password: '))
        userInfo = {'username':username, 'password':password}
        saveInfoFlag = raw_input("Do you want me to save the username"
                                 " and password(y/n): ")
        if saveInfoFlag.lower()[:1] == 'y':
            f = open('info','w')
            f.write(str(userInfo))
            f.close()
    return userInfo
    
