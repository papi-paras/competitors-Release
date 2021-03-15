from selenium.webdriver.common.by import By


class MEmuObjects():

    allarticles = (By.XPATH, "//section[@id='primary']/div/article")
    Title = (By.XPATH, "//h1[@class='entry-title']")
    completenotes = (By.CSS_SELECTOR, "div[class='entry-content']")
    releasenoteslink = "For more detailed article please visit: " + "http://www.memuplay.com/blog/en/category/release-notes"
    installerlink = "App player Installer can be found here:" + "https://www.memuplay.com/download-memu-on-pc.html?from=offline_installer"
    articledate = (By.XPATH, "//time[@class='entry-date published']")

    def __init__(self, driver):
        self.driver = driver

    def returnallartiles(self):
        return self.driver.find_elements(*MEmuObjects.allarticles)

    def returnpagetitle(self):
        return self.driver.find_element(*MEmuObjects.Title)

    def returnreleasenotes(self):
        return self.driver.find_element(*MEmuObjects.completenotes)

    def returnreleasenoteslink(self):
        return MEmuObjects.releasenoteslink

    def returninstallerlink(self):
        return MEmuObjects.installerlink

    def returnarticledate(self):
        return self.driver.find_element(*MEmuObjects.articledate)