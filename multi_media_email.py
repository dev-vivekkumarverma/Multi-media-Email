
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import ssl
import os


# print(student_names)
def send_test_mail(student_name,receiver_email,file_name,body):
    sender_email = "#sender's mail"
    password="#password obtained after registring your app for two factor authentication in sender email's google setting"
    msg = MIMEMultipart()
    msg['Subject'] = "#email subject"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    # for text file
    # filename = "example.txt"
    # msg.attach(MIMEText(open(filename).read()))

    #for image files
    # with open('example.jpg', 'rb') as fp:
    #     img = MIMEImage(fp.read())
    #     img.add_header('Content-Disposition', 'attachment', filename="example.jpg")
    #     msg.attach(img)
        
    pdf = MIMEApplication(open(file_name, 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename= "#file_name")
    msg.attach(pdf)

    try:
        context=ssl.create_default_context()
        # print("ssl context, created...")
        with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465,context=context) as smtp:
            # smtpObj.ehlo()
            # smtpObj.starttls()
            smtp.login(user=sender_email,password=password)
            smtp.sendmail(sender_email, receiver_email, msg.as_string())
            return "{} sent to {}".format(pdf.get_filename(),receiver_email)
    except Exception as e:
        print(e)


body="""body of email"""

print(send_test_mail(student_name="#name of receiver",receiver_email=str("#email of receiver").strip(),file_name="#file path", body=body))
