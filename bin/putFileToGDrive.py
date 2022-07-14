from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication



def putFileToGoogle():

    gauth = GoogleAuth()

    gauth.CommandLineAuth()

    drive = GoogleDrive(gauth)
    
    # Set the path of HKT target file
    ReportPath = "../Shell/Report/Decrypt/"

    try:

         # Search the folder for Excel file
            for file in os.listdir(ReportPath):

                print(file)

                gfile = drive.CreateFile({'parents': [{'id': '1iGta9hW7wODh6AKea3D4Sm1on5fTETTR'}]})

                gfile['title'] = file
        
                gfile.SetContentFile(ReportPath + file)

                gfile.Upload()

        
    except:

        emailsubject = "Asia Mile Fulfillment - error found on uploading file to Goolge drive!"

        sendMessage(emailsubject)

        print(emailsubject)


def sendMessage(emailsubject):
   
    SENDER = "Elegant Technologies <gary.twyeung@gmail.com>"

    RECIPIENT = "gary@elegant.com.hk"

    # Specify a configuration set
    CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-west-2"

    # The subject line for the email.
    SUBJECT = emailsubject

    
        # The full path to the file that will be attached to the email.
    ATTACHMENT = "\log\AM_log.txt"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = "Hello,\r\nPlease see the attached log file."

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


        
putFileToGoogle()

