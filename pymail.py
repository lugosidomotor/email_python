import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


sender_email = ""
receiver_email = ""

msg = MIMEMultipart()
msg['Subject'] = '[Email Test]'
msg['From'] = sender_email
msg['To'] = receiver_email

msgText = MIMEText('Hello')
msg.attach(msgText)

pdf = MIMEApplication(open("example.pdf", 'rb').read())
pdf.add_header('Content-Disposition', 'attachment', filename= "example.pdf")
msg.attach(pdf)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtpObj:
        smtpObj.login("user", "pwd")
        smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
except Exception as e:
    print(e)
