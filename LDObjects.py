from selenium.webdriver.common.by import By


class LDObjects():

    get_all_dates = (By.XPATH, "//div[@class='left']/span")
    get_all_dates2 = (By.XPATH, "//div[@class='left']/span[2]")
    get_string1 = "For more detailed article please visit: " + "https://www.ldplayer.net/other/version-history-and-release-notes.html"
    get_releasenotes_text = (By.XPATH, "//div[@class='bottom-msg']/p")
    get_playerversion = (By.XPATH, "//div[@class='top-msg']")

    def __init__(self, driver):
        self.driver = driver

    def returnalldates(self):
        return self.driver.find_elements(*LDObjects.get_all_dates)

    def returnalldates2(self):
        return self.driver.find_elements(*LDObjects.get_all_dates2)

    def returnstring1(self):
        return LDObjects.get_string1

    def returnreleasenotetext(self):
        return self.driver.find_element(*LDObjects.get_releasenotes_text)

    def returnplayerversion(self):
        return self.driver.find_element(*LDObjects.get_playerversion)