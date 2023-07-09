import smtplib
from email.mime.multipart import MIMEMultipart as mmp
from email.mime.text import MIMEText as mtext

from_addr = 'ekatherinered@gmail.com'
to_addr = ['anastasiavvol@gmail.com', 'ekatherinered@gmail.com']
msg = mmp()
msg['From'] = from_addr
msg['To'] = to_addr
msg['subject'] = 'проверочное'
body = 'привет'

msg.attach(mtext(body, 'plain'))
email = ""
password = ""

mail = smtplib.SMTP('smpt.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()