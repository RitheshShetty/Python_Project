from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'ritheshshetty94@gmail.com'
email_password = 'btendzbhcpxgbbjv'

email_receiver = 'ritheshshetty555@gmail.com'

subject = 'Email Sender Project'

body = "Hi All, \n writing the mail\n\n" \
       "Thanks and Regards,\n" \
       "Rithesh Shetty"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())