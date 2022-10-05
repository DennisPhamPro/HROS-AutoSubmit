from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from log import Log
import pathlib

######################################################
chromedriver_autoinstaller.install()
##########################################################
script_directory = pathlib.Path().absolute()
path = str(script_directory) + "/log/" #Enter your path log here
log = Log(path)
########################################################
class HRMS:
    def __init__(self, chrome_options):
        self._driver = webdriver.Chrome(options=chrome_options)

    def get_url(self, url : str):
        self.url = "https://"+ url
        self._driver.get(self.url)
        self._driver.implicitly_wait(5)
        log.Write_Info("Done get URL")
        
    def login(self, login_info):
        #find login button
        WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Terralogic Login']"))).click()

        #enter email
        email_input = WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email_input.send_keys(login_info[0])
        email_input.send_keys(Keys.ENTER)

        #enter password
        pw_input = WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.NAME, "password")))
        pw_input.send_keys(login_info[1])
        pw_input.send_keys(Keys.ENTER)
        log.Write_Info("Done logging")

class Timesheet(HRMS):
    def __init__(self, chrome_options):
        super().__init__(chrome_options)

    def timesheet(self,data):
        week = 0
        #nav and click timesheet
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'content')]//a[contains(@href,'sheet')]"))).click()
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'AppFooter')]"))).click()   

        while week < len(data['Week']):
        #nav and click add task
            WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ant-btn')]/img"))).click()

            #enter date
            date = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_dates")))
            date.send_keys(data['Start'][week])
            end = self._driver.find_element(By.XPATH, "//input[@placeholder='End date']")
            end.send_keys(data['End'][week])
            end.send_keys(Keys.ENTER)

            #enter project
            pro = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_projectId")))
            pro.send_keys(data['Project'][week])
            pro.send_keys(Keys.BACKSPACE)
            pro.send_keys(Keys.ENTER)

            #enter task
            WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_taskName"))).send_keys(data['Task'][week])

            #check time out
            tout = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_endTime")))
            tout.send_keys("5:00 pm")
            tout.send_keys(Keys.ENTER)

            #writing some description 
            WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_notes"))).send_keys(data['Description'][week])

            #click close
            WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-link']/span"))).click()

            week+=1
