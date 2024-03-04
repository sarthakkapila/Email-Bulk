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
We hope this invitation message finds you well. As a valued member of our alma mater's esteemed community, we're exhilarated to reconnect with you and share some exciting developments from the Entrepreneurship and Incubation Cell (EIC) at PEC.

The EIC has been a pivotal force in fostering entrepreneurship and innovation within our alma mater since its inception in 2015. Under the Ministry of Education's Innovation Cell Programs, we've been instrumental in supporting startups through alumni networks, seed capital and a range of invaluable resources and opportunities.

Our flagship event, the E-Summit, plays a significant role in bringing together budding entrepreneurs, industry leaders, investors and professionals to collaborate, innovate and drive meaningful change. The summit not only provides a platform for startups to showcase their ventures but also offers a plethora of enriching experiences, including Funding Conclave, Startup Expo, Expert Sessions, Intern Fair and many more.

Our Expectation:
Your invaluable contribution, through any of the possible means such as sponsorship, personal funding, guidance or sharing your insights to varied audience as a speaker, will play a pivotal role in shaping the success of E-SUMMIT 2024. Your support will be a wellspring of inspiration and encouragement for our students..
We invite you to be a part of this exciting entrepreneurial journey by:
Contributing to the event's success through sponsorships and personal grants.
We extend a warm invitation for you to participate in this premier business gathering by sponsoring or funding a selection of our events, which will engage over 200 participants from various institutions. This valued collaboration will benefit us immensely in fostering the new generation of entrepreneurs.
Share insights as a contributing guest speaker.
Join EIC Tribe, an alumni initiative, in empowering aspiring student entrepreneurs through mentorship and support for their startup ventures.
Become a Mentor.
Step into the role of a guide, offering support to startups within the EIC incubator and students striving to incubate their own ventures.

Become an investor.
Be a part of our young entrepreneur start-up journey by financially supporting PEC's startups and helping them to achieve new milestones.
With your support and participation, we have been able to achieve significant milestones, including:

Incubating 6 startups to date
Awarding cash prizes totalling over 50,000 in various competitions, including IPL Auction and Build Pitch, among others
Garnering a participation of 5,000+ attendees in the last two E-Summits
Hosting 30+ speaker sessions featuring industry experts
Welcoming over 10,000 total footfalls at our events

We firmly believe that our alumni community plays a pivotal role in shaping the future of entrepreneurship at PEC. Your expertise, insights and contributions are invaluable assets that can empower our current students and startups to thrive in today's dynamic landscape.

Kindly convey your thoughts and availability by replying to this email or contacting us at 9877890340. We eagerly await the opportunity to join forces and create a spectacular E-SUMMIT 2024 that will become a legacy to continue.
Thank you for your time, consideration, and continued support. Let's make E-SUMMIT 2024 a grand success together!
PFA the brochure of E-SUMMIT 2024 for more insights.
Warm regards,

Ansh Ohri
Head Alumni and Industry Relations
E-SUMMIT 2024
9877890340

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
