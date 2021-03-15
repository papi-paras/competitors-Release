from Connection import Connectionclass
from LDObjects import LDObjects
import datetime
import smtplib
import os
from email.message import EmailMessage


class TestLDnotes(Connectionclass):
    def test_LD(self):
        LDplayerobjects = LDObjects(self.driver)
        all_dates = LDplayerobjects.returnalldates()
        all_dates2 = LDplayerobjects.returnalldates2()
        todays_date = datetime.date.today().strftime('%d %Y-%m')

        for dates in all_dates:
            dates.text
            break
        for dates2 in all_dates2:
            dates2.text
            break

        string1 = LDplayerobjects.returnstring1()
        releasenotestext = LDplayerobjects.returnreleasenotetext().text
        playerversion = LDplayerobjects.returnplayerversion().text

        emailAddress = os.environ.get("EMAIL_ADDRESS")
        emailPassword = os.environ.get("EMAIL_PASSWORD")
        msg = EmailMessage()
        msg['Subject'] = "A New LDplayer Has Arrived!"
        msg['From'] = emailAddress
        msg['To'] = emailAddress
        msg.set_content("Whats New in " + playerversion + " here: https://www.ldplayer.net/" + '\n\n' + releasenotestext + '\n\n' + string1)
        if todays_date != dates.text + " " + dates2.text:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(emailAddress, emailPassword)
                smtp.send_message(msg)

        self.driver.close()
