from getFileFromGoogleDrive import getFileFromGoogle
from DropnaExcel import Excel2Text
from Pythonsftp import uploadAMFile
import shutil
import os
import time

# Google Drive ID of the source file located
googleFolder = '1zTEFYibhbQsZMcyukghxPspxl0T3vN-q'

# Get current path of the script file
currentPath = os.path.dirname(os.path.realpath(__file__))

# path of the source file retrieved from Google drive
exeFolder    = currentPath+'/file/'


try:

    # run function to retrieve file from Google Drive
    getFileFromGoogle(googleFolder,exeFolder)


    # if file exists at the folder
    if os.listdir(exeFolder):

        # run function to replace empty space in the Excel file
        Excel2Text(exeFolder,currentPath)

        # upload encrypted file
        uploadAMFile(exeFolder,currentPath)

        # delete the Excel file
        for file in os.listdir(exeFolder):
                           
            os.remove(exeFolder + file)


except:

    # send error email to admin
    os.system("python ErrorMessage.py")






