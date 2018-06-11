import json
from sys import platform
import sys
import MySQLdb

def sysTest():
    #Check if database connectivity exists
    try:
        db = MySQLdb.connect(getConfig()['database'][getOS()]['host'], 
                             getConfig()['database'][getOS()]['username'], 
                             getConfig()['database'][getOS()]['password'],
                             getConfig()['database'][getOS()]['db'])
        db.close()
    except Exception as e:
        print(e)
        return False
        
    
    return True
    
    
def getOS():
    
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "OSX"
    elif platform == "win32":
        return "windows"
    
def getConfig():
    #Get values like
    #print(data['database']['windows']['host'])
    with open('./includes/config.json') as f:
        data = json.load(f)
    return data
    
    
    
