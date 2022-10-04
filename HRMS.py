from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from log import Log
from datetime import datetime
import pathlib

######################################################
chromedriver_autoinstaller.install()
##########################################################
script_directory = pathlib.Path().absolute()
path = script_directory + "/log/" + str(datetime.now().strftime('%Y_%M_%d_%H_%M_%S')) + ".log"
log = Log(path)
########################################################
class HRMS:
    def __init__(self, chrome_options):
        self._driver = webdriver.Chrome(options=chrome_options)

    def get_url(self, url : str):
        self.url = "https://"+ url
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        log.Write_Info("Done get URL")
        
    def login(self, login_info):
        #find login button
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Terralogic Login']"))).click()

        #enter email
        email_input = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email_input.send_keys(login_info[0])
        email_input.send_keys(Keys.ENTER)

        #enter password
        pw_input = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME, "password")))
        pw_input.send_keys(login_info[1])
        pw_input.send_keys(Keys.ENTER)
        log.Write_Info("Done logging")