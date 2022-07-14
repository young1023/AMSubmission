from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
import os
import time


# Google Drive ID of the source file located
googleFolder = '1zTEFYibhbQsZMcyukghxPspxl0T3vN-q'

# Get current path of the script file
currentPath = os.path.dirname(os.path.realpath(__file__))

# path of the source file retrieved from Google drive
exeFolder    = currentPath+'/file/'

def getFileFromGoogle(googleFolder,exeFolder):

    gauth = GoogleAuth()

    gauth.CommandLineAuth()

    drive = GoogleDrive(gauth)

    # access Google drive Attachment folder and download file
    file_list = drive.ListFile({'q': "'"+googleFolder+"' in parents and trashed=false"}).GetList()

    #Search the folder
    for file in file_list:
        
        file.GetContentFile(file["title"], mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        time.sleep(5)

        if os.path.exists(file["title"]):

            # Move file to Asia Miles folder
            shutil.move(file["title"],exeFolder)

    
     # Search the folder
    for file in file_list:

        # delete the file at Google Drive
        file.Delete()

    if not os.path.exists(exeFolder):
        time.sleep(5)

   
getFileFromGoogle(googleFolder,exeFolder)


