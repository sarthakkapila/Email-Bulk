import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

csv_file = "recipients_trial.csv"
pdf_file = "E-Summit Brochure.pdf"

data = pd.read_csv(csv_file)

server = 'smtp.gmail.com'
port = 587
username = 'mehak.eic.alumnirelations@gmail.com'
password = "YOUR_APP_PASSWORD"

server = smtplib.SMTP(server, port)
server.starttls()
server.login(username, password)

sender = 'mehak.eic.alumnirelations@gmail.com'
subject = """Contribute to PEC's Entrepreneurial Ecosystem!"""
body = """
Respected {{Name}},
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



"""

for index, row in data.iterrows():
    recipient_name = row["Name"]
    recipient_email = row["Email"]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient_email
    msg['Subject'] = subject

    body_formatted = body.replace('{{Name}}', recipient_name)

    msg.attach(MIMEText(body_formatted, 'plain'))

    with open(pdf_file, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header('content-disposition', 'attachment', filename=pdf_file)
        msg.attach(pdf_attachment)


    server.send_message(msg)

server.quit()
