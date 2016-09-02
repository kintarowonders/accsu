global testing
global webDirScript
global addUserGroups
global userListPath
global userAddCmd
global siteAddCmd

testing = True
webDirScript = "create-website.bash"
addUserGroups = "users"
userListPath = "userlist"
domainListPath = "domainlist"
userAddCmd = "echo useradd -m -G users %USER%"
siteAddCmd = "echo /root/create-website.bash %USER% %DOMAIN% %DIR%"
