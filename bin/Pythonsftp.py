import os
import io
import pysftp
import shutil
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Get current path of the script file
currentPath = os.path.dirname(os.path.realpath(__file__))

# path of the source file retrieved from Google drive
exeFolder    = currentPath+'/file/'


def uploadAMFile(exeFolder,currentPath):

    try:

        # Establish sftp connection
        myHostname = "mft-prd.cathay​pacific.com"          #production sFTP
        #myHostname = "mft-pat.ete.cathaypacific.com"       #UAT

        myUsername = "shell_prd"                          #production account   
        #myUsername = "shell_ete"                           #UAT Account

        myPassword = "S$H/E$L#L%_pwd"                      #production password
        #myPassword = "S$H/E$L#L%_pwd"                       #UAT password

        cnopts = pysftp.CnOpts()

        cnopts.hostkeys = None  

        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:

            sftp.cwd('/from-SZ')
    
            sftp.put(exeFolder+'sz4.txt.gpg')

            print('Date: ' + str(datetime.now()) + ' Directory listing at sFTP server' , file=open(currentPath+"\log\AM_log.txt", "w"))

            print(sftp.listdir(), file=open(currentPath+"\log\AM_log.txt", "a"))

            emailSubject =  str(sftp.listdir()) + ' uploaded on ' + str(datetime.now().strftime("%c"))
 
            #print(sftp.listdir())      # for debugging

            sftp.close()

        sendMessage(emailSubject,exeFolder)


    except:

        emailSubject = " - error found on uploading"

        sendMessage(emailSubject,exeFolder)


def sendMessage(emailSubject,exeFolder):
   
    SENDER = "Elegant Technologies Limited <gary.twyeung@gmail.com>"

    RECIPIENT = "gary@elegant.com.hk"

    # Specify a configuration set
    CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-west-2"

    # The subject line for the email.
    SUBJECT = "Asia Miles file " + emailSubject

    # The full path to the file that will be attached to the email.
    ATTACHMENT = exeFolder + "SZ4.txt"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = "Hello,\r\nPlease check."

    # The HTML body of the email.
    BODY_HTML = """\
    <html>
    <head></head>
    <body>
    <p>Hi,</p>
    <p>Please see the attached log file.</p>
    </body>
    </html>
    """

    # The character encoding for the email.
    CHARSET = "utf-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT 
    msg['From'] = SENDER 
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    # Add the attachment to the parent container.
    msg.attach(att)
    #print(msg)
    try:
        #Provide the contents of the email.
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=[
                RECIPIENT
            ],
            RawMessage={
                'Data':msg.as_string(),
            },
            ConfigurationSetName=CONFIGURATION_SET
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


#uploadAMFile(exeFolder,currentPath)

   

    


