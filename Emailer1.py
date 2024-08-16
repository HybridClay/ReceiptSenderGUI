#Being able to at least send an email with python
#From YT: "How to send Emails with Python [New Method 2023]" by The PyCoach
from email.message import EmailMessage
import ssl
import smtplib

email_sender = '@MyEmailHere'
email_password = ''
email_receiver = '@MyEmailHere'

subject = 'Client Name - Balance sheet'
body = """
Good morning,

Here is your balance sheet

kind regards.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    smtp.send_message()



