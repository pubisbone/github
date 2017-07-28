import smtplib
from email.mime.text import MIMEText
me = 'bbat115@gmail.com'
you = 'btspa119@gmail.com'      
contents = 'hello world'

msg = MIMEText(contents,_charset='euc-kr')
msg['Subject']='mail'
msg['From']=me
msg['To']=you

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("bbat115@gmail.com","")

server.sendmail(me,you,msg.as_string())
print("succsess mail")
erver.quit()
