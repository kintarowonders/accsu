import os
import accsuGlobals

def sanitizeCmd(cmd):
    newcmd = ""
    for char in cmd:
        okay=False
        cint = ord(char)
        if (cint >= 30 && cint <= 39):
            okay=True
        if (cint >= 65 && cint <= 90):
            okay=True
        if (cint >= 97 && cint <= 122):
            okay=True
        if (cint == 46):
            okay=True
        if (okay):
            newcmd = newcmd + chr(cint)
    return cmd

def domainExists(domain):
    f = open(accsuGlobals.domainListPath,"r")
    for line in f:
        if (user == line):
        f.close()
        return True
    f.close()
    return False

def domainListAdd(domain):
    f = open(accsuGlobals.domainListPath,"w")
    f.write(domain + "\n")
    f.close()

def userExists(user):
    f = open(accsuGlobals.userListPath,"r")
    for line in f:
        if (user == line):
            f.close()
            return True
    f.close()
    return False

def userListAdd(user):
    f = open(accsuGlobals.userListPath,"w")
    f.write(user + "\n")
    f.close()

def newUser(arguments):
    try:
        user = arguments["user"]
        password = arguments["pass"]
    except NameError:
        return True
    if (userExists(user) == True):
        return True
    if (accsuGlobals.testing == True):
        print ("DBG: newUser: Adding user", user)
        return False
    userListAdd(user)
    shellCmd = accsuGlobals.userAddCmd
        shellCmd.replace("%USER%", user)
    shellCmd = sanitizeCmd(shellCmd)
    os.system(shellCmd)
    return False
    
def newSite(arguments):
    try:
        user = arguments["user"]
        domain = arguments["domain"]
        path = arguments["path"]
    except NameError:
        return True
    if (userExists(user) == 1):
        return True
    if (os.path.isdir(path)):
        return True
    if (domainExists(domain)):
        return True
    if (accsuGlobals.testing == True):
        print ("DBG: newSite: Adding site " + user + " " + domain + " " + path)
        return False
    domainListAdd(domain)
    shellCmd = accsuGlobals.siteAddCmd
        shellCmd.replace("%USER%",user)
        shellCmd.replace("%DOMAIN%",domain)
        shellCmd.replace("%DIR%",path)
    shellCmd = sanitizeCmd(shellCmd)
    os.system(shellCmd)
    return False

def command(command, arguments):
    commands = {
        newuser: newUser,
        newsite: newSite,
    }
    
    func = commands.get(command)

    return func()
