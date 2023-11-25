import smtplib

from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()

server.login('brandonforku@gmail.com', '(2*2=4and5+3=8iSfOrMuLlUhTeKwI)')
msg = MIMEMultipart()
msg['From'] = 'mr forku brandon'
msg['To'] = 'forkubrandon13@gmail.com'
msg['Subject'] = 'wrtting in  python programming language'
msg['Text'] = 'hello every one this meassage was send true python programming language'

"""
filename = 'the name of the file'
attachement = open(fileanme, rb)

p= MIMEBase('application', 'octet_stream')
p.set_payload(payload)
encoders.encode_base64(p)
p.add_header('content disposition', f"attachment; filename(filename)")
msg.attach(p)

"""
text = msg.ss_string()
server.sendmail('brandonforku@gmail.com', 'forkubrandon13@gmail.com', text)