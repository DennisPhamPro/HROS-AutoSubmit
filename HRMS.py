import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import logging
import time 
######################################################
chromedriver_autoinstaller.install()
######################################################
chrome_options = Options()
#chrome_options.add_argument("--logging eadless")
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
        time.sleep(2)

class Timesheet(HRMS):
    def __init__(self):
        pass
    def timesheet(self,data):
        week = 0
        #nav and click timesheet
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'content')]//a[contains(@href,'sheet')]"))).click()
        # hover.click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'AppFooter')]"))).click()   
        while week < len(data['Week']):
            #nav and click add task
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ant-btn')]/img"))).click()
            #enter date
            date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_dates")))
            date.send_keys(data['Start'][week])
            end = driver.find_element(By.XPATH, "//input[@placeholder='End date']")
            end.send_keys(data['End'][week])
            end.send_keys(Keys.ENTER)

            #enter project
            pro = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_projectId")))
            pro.send_keys(data['Project'][week])
            pro.send_keys(Keys.BACKSPACE)
            pro.send_keys(Keys.ENTER)

            #enter task
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_taskName"))).send_keys(data['Task'][week])

            #check time out
            tout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_endTime")))
            tout.send_keys("5:00 pm")
            tout.send_keys(Keys.ENTER)

            #writing some description 
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_notes"))).send_keys(data['Description'][week])

            #click close
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-link']/span"))).click()

            week+=1