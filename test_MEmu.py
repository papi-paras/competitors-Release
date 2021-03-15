from Connection import Connectionclass
from MEmuObjects import MEmuObjects
import datetime
import smtplib
import os
from email.message import EmailMessage


class TestMEmunotes(Connectionclass):
    def test_MEmu(self):
        MEmuplayerobjects = MEmuObjects(self.driver)
        articles = MEmuplayerobjects.returnallartiles()
        for article in articles:
            article.find_element_by_xpath("div/div").click()
            break
        pageTitle = MEmuplayerobjects.returnpagetitle().text
        pageBody = MEmuplayerobjects.returnreleasenotes().text
        string1 = MEmuplayerobjects.returnreleasenoteslink()
        string2 = MEmuplayerobjects.returninstallerlink()
        article_date_str = MEmuplayerobjects.returnarticledate().text
        todays_date = datetime.date.today().strftime('%B %d, %Y')

        emailAddress = os.environ.get("EMAIL_ADDRESS")
        emailPassword = os.environ.get("EMAIL_PASSWORD")
        msg = EmailMessage()
        msg['Subject'] = pageTitle
        msg['From'] = emailAddress
        msg['To'] = emailAddress
        msg.set_content(pageBody + '\n\n' + string1 + '\n' + string2)

        if todays_date != article_date_str:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(emailAddress, emailPassword)
                smtp.send_message(msg)
