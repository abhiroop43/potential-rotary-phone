import requests
import os
from bs4 import BeautifulSoup
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

# email content placeholder
content = ""


# extracting the Hacker News stories
def extract_news(url):
    print("Extracting Hacker News Stories...")
    extracted_content = ""
    extracted_content += ("<b>HN Top Stories:</b>\n" + "<br>" + "-" * 50 + "<br>")
    response = requests.get(url)
    news_content = response.content
    soup = BeautifulSoup(news_content, "html.parser")

    for i, tag in enumerate(soup.find_all("td", attrs={"class": "title", "align": ""})):
        extracted_content += ((str(i + 1) + " :: " + tag.text + "\n" + "<br>") if tag.text != "More" else "")
        # print(tag.prettify) # find all('span', attrs={'class':'sitestr'})
    return extracted_content


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += "<br>------------------<br>"
content += "<br><br>End of Message"

# send the email

print("Composing email.......")

# email configuration

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.environ['EMAIL_ID']
TO = [os.environ['EMAIL_ID']]
PASS = os.environ['GOOGLE_APP_PASSWORD']

# fp = open(file_name, 'rb')

# create text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = f"Top News Stories HN [Automated Email] {str(now.day)}-{str(now.month)}-{str(now.year)}"
msg['From'] = FROM
msg['To'] = ", ".join(TO)

msg.attach(MIMEText(content, 'html'))

# fp.close()

print("Initializing server.......")

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP_SSL(SERVER, 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email sent.......")

server.quit()

