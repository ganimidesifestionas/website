# email_services/email_services.py
#import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .. import app
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
#import sendgrid
#from sendgrid.helpers.mail import *

def send_email(parTo,parSubject,parContentHtml,parContentText='',parContentTemplate=''):
    appFrom="noreply@ganimides.com"
    if not(parTo):
        app.logger.info('   %s No Recipient', 'send_email')
        return('No Recipient')
    if not(parSubject):
        app.logger.info('   %s No Subject', 'send_email')
        return('No Subject')
    if not(parContentHtml) and not(parContentText) and not(parContentTemplate):
        app.logger.info('   %s No Content', 'send_email')
        return('No Content')
    try:
        if (1==1):
            result=sendEmail_thru_google(appFrom,parTo,parSubject,parContentHtml,parContentText,parContentTemplate)
        else:
            result=sendEmail_thru_sendgrid(appFrom,parTo,parSubject,parContentHtml,parContentText,parContentTemplate)
    except Exception as error_text:
        result=error_text

    print('@@@^^^@@@ sendEmail:',result)
    return(result)


def sendEmail_thru_google(parFrom,parTo,parSubject,parContentHtml,parContentText='',parContentTemplate=''):
    """
    sendEmail_thru_google
    """
    if not(parFrom):
        parFrom="noreply@ganimides.com"

    if not(parTo):
        app.logger.info('      %s recipient not defined', 'sendEmail_thru_google')
        return 'recipient not defined'
    if not(parSubject):
        app.logger.info('      %s subject not defined', 'sendEmail_thru_google')
        return 'subject not defined'
    if not(parContentHtml) and not(parContentText) and not(parContentTemplate):
        app.logger.info('      %s content or template not defined', 'sendEmail_thru_google')
        return 'content or template not defined'

    try:
        msg=FormattedEmailMessage(parFrom,parTo,parSubject,parContentHtml,parContentText,parContentTemplate)
        if not(msg):
            app.logger.info('      %s can not format email message', 'sendEmail_thru_google')
            return 'can not format email message'
    except Exception as error_text:
        app.logger.info('      %s exception:%s', 'sendEmail_thru_google',error_text)
        return error_text

    try:
        print('@@@^^^@@@ sendEmail_thru_google start------------------------------------')
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        #mail.login('bstarr131@gmail.com', 'bstarr13')
        mail.login('scantzochoiros@gmail.com', 'philea13')
        mail.sendmail(parFrom, parTo, msg.as_string())
        mail.quit()
        print('@@@^^^@@@ sendEmail_thru_google finish-----------------------------------')

        #echo "export SENDGRID_API_KEY='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'" > sendgrid.env
        #echo "sendgrid.env" >> .gitignore
        #source ./sendgrid.env

        #SENDGRID_API_KEY='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'
        #sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        #parFrom="noreply@ganimides.com"
        #from_email = Email(parFrom)
        #to_email = Email(parTo)
        #subject = parSubject
        #content = Content("text/plain", "and easy to do anywhere, even with Python")
        #mail = Mail(from_email, subject, to_email, content)
        #response = sg.client.mail.send.post(request_body=mail.get())
        #print('response.status_code=',response.status_code)
        #print('response.body=',response.body)
        #print('response.headers=',response.headers)

        #thisService.set_result('OK')
    except Exception as error_text:
        print('@@@^^^@@@ sendEmail_thru_google ERROR:',error_text)
        return error_text

    return 'OK'

def sendEmail_thru_sendgrid(parFrom,parTo,parSubject,parContentHtml,parContentText='',parContentTemplate=''):
    """
    sendEmail_thru_sendgrid
    """
    if not(parFrom):
        parFrom = "myBank@ganimides.com"

    if not(parTo):
        return 'recipient not defined'
    if not(parSubject):
        return 'subject not defined'
    if not(parContentHtml) and not(parContentText) and not(parContentTemplate):
        return 'content or template not defined'

    try:
        #echo "export SENDGRID_API_KEY='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'" > sendgrid.env
        #echo "sendgrid.env" >> .gitignore
        #source ./sendgrid.env
        #SENDGRID_API_KEY='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'
        #sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        #parFrom="noreply@ganimides.com"
        #from_email = Email(parFrom)
        #to_email = Email(parTo)
        #subject = parSubject
        #content = Content("text/plain", "and easy to do anywhere, even with Python")
        #mail = Mail(from_email, subject, to_email, content)
        #response = sg.client.mail.send.post(request_body=mail.get())
        # print('response.status_code=', response.status_code)
        # print('response.body=', response.body)
        # print('response.headers=', response.headers)
        return 'OK'
    except Exception as error_text:
        return error_text

def FormattedEmailMessage(parFrom,parTo,parSubject,parContentHtml,parContentText='',parContentTemplate=''):
    # Create message container - the correct MIME type is multipart/alternative.
    print('@@@@@@@@@@FormattedEmailMessage')
    if not(parFrom):
        parFrom = "myBank@ganimides.com"
    if not(parTo):
        return(None)
    if not(parSubject):
        return(None)
    if not(parContentHtml) and not(parContentText) and not(parContentTemplate):
        return(None)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = parSubject
    msg['From'] = parFrom
    msg['To'] = parTo

    if parContentTemplate=='x':
        # Create the body of the message (a plain-text and an HTML version).
        parContentText = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        parContentHtml = """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.

    # Record the MIME types of both parts - text/plain and text/html.
    if parContentText:
        part1 = MIMEText(parContentText, 'plain')
        msg.attach(part1)
    if parContentHtml:
        part2 = MIMEText(parContentHtml, 'html','utf8')
        msg.attach(part2)

    return msg