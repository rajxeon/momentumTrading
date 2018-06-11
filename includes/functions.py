import json
from sys import platform
import sys
import MySQLdb
import warnings

def sysTest():
    #Check if database connectivity exists
    try:
        db=createConnection()
        db.close()
    except Exception as e:
        print(e)
        return False
    
    setUpTables()
    return True

def createConnection():
     db = MySQLdb.connect(getConfig()['database'][getOS()]['host'], 
                             getConfig()['database'][getOS()]['username'], 
                             getConfig()['database'][getOS()]['password'],
                             getConfig()['database'][getOS()]['db'])
     return db
    
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


def setUpTables():
    db=createConnection()
    cursor = db.cursor() 
    for query in getConfig()['queries']:
        with warnings.catch_warnings(record=True) as w:
            cursor.execute(query)            
            db.commit()
            if len(w)>0:
                message=(w[-1].message)
                print((message))
            else:
                a=query
                print("New table created:"+a[a.find('`')+1:27+a[a.find('`')+1:].find('`')+1])
    
    db.close()
    

