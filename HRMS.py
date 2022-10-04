import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import logging 
######################################################
chromedriver_autoinstaller.install()
######################################################
chrome_options = Options()
#chrome_options.add_argument("--i logging eadless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
###########################################################
logging.basicConfig(filename='Bruh_logging.log',format= '%(asctime)s : %(levelname)s :\
 %(lineno)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
 ##########################################################
chrome_options.page_load_strategy = 'normal' 
driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
########################################################
class HRMS:
    def __init__(self):
        pass
    def get_url(self,url : str):
        self.url = "https://"+ url
        driver.get(self.url)
        driver.implicitly_wait(5)
        logging.info("Done get URL")
    def login(self,login_info):
        #find login button
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Terralogic Login']"))).click()
        #enter email
        email_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email_input.send_keys(login_info[0])
        email_input.send_keys(Keys.ENTER)
        #enter password
        pw_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME, "password")))
        pw_input.send_keys(login_info[1])
        pw_input.send_keys(Keys.ENTER)
        logging.info("Done logging")
        # driver.close()

        