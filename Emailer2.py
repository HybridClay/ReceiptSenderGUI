#Being able to send an email with an attachment
#FRom YT: "How to Send Emails with Attachments using Python" by codewithabdul

#smtplib provides functionality to send emails using SMTP
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data to email
from email.mime.application import MIMEApplication

email_sender = '@MyEmailHere'
email_password = ''
email_receiver = '@MyEmailHere'
subject = 'Client Name - Balance sheet'
body = """Good morning,

Here is your balance sheet

kind regards"""

smtp_server = 'smtp.gmail.com'
smtp_port = 465
path_to_file = 'Sample - Balance Practice.pdf'

message = MIMEMultipart()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject
body_part = MIMEText(body)
message.attach(body_part)
 
with open(path_to_file, 'rb') as file:
    #Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name="Sample - Balance Practice.pdf"))
    
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, message.as_string())
print("Email Sent!")

