from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from log import Log
import pathlib

##########################################################
chromedriver_autoinstaller.install()
##########################################################
script_directory = pathlib.Path().absolute()
path = str(script_directory) + "/log/" #Enter your path log here
log = Log(path)
##########################################################
class HRMS:
    '''General funcionality for HR-OS'''

    def __init__(self, chrome_options):
        self._driver = webdriver.Chrome(options=chrome_options)

    def get_url(self, url : str):
        try:
            self.url = "https://"+ url
            log.Write_Info("Navigating to {}...".format(self.url))
            self._driver.get(self.url)
            self._driver.implicitly_wait(5)
            log.Write_Info("Done get URL")
        except Exception as e:
            log.Write_Error("Cannot navigate to {} (maybe URL is not valid). Error detail is as below.".format(self.url))
            log.Write_Error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))

    def login(self, login_info):
        try:
            #find login button
            WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Terralogic Login']"))).click()
        except Exception as e:
            log.Write_Error("Cannot click onto login button. Error detail is as below.")
            log.Write_Error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))

        try:
            log.Write_Info("Try logging to HROS by TL account.")    
            #enter email
            email_input = WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.ID, "identifierId")))
            email_input.send_keys(login_info[0])
            email_input.send_keys(Keys.ENTER)
        except Exception as e:
            log.Write_Error("Cannot type email. Error detail is as below.")
            log.Write_Error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))

        try:
            #enter password
            pw_input = WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.NAME, "password")))
            pw_input.send_keys(login_info[1])
            pw_input.send_keys(Keys.ENTER)
        except Exception as e:
            log.Write_Error("Cannot type password (Wrong email or xpath not found). Error detail is as below.")
            log.Write_Error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))

        try:
            WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='logo']")))
            log.Write_Info("Done logging")
        except:
            log.Write_Error("Cannot login to HROS. Wrong password.")
            

class Timesheet(HRMS):
    '''Timesheet functionality : Tasks, submissions,...'''
    def __init__(self, chrome_options):
        super().__init__(chrome_options)

    def timesheet(self):
        #nav and click timesheet
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'content')]//a[contains(@href,'sheet')]"))).click()
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'AppFooter')]"))).click()   
        log.Write_Info("Done navigate to TimeSheet")

    def submit(self, date_start: str, date_end: str, start_time: str, end_time: str, project: str, task: str, description: str):
        """date_format: MM/DD/YY, time_format: 8:00 am"""

        log.Write_Info("Try adding TimeSheet")
        #nav and click add task
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ant-btn')]/img"))).click()

        #enter date
        date = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_dates")))
        date.send_keys(date_start)
        end = self._driver.find_element(By.XPATH, "//input[@placeholder='End date']")
        end.send_keys(date_end)
        end.send_keys(Keys.ENTER)

        #check time in
        tin = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_startTime")))
        tin.send_keys(start_time)
        tin.send_keys(Keys.ENTER)

        #check time out
        tout = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_endTime")))
        tout.send_keys(end_time)
        tout.send_keys(Keys.ENTER)

        #enter project
        pro = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_projectId")))
        pro.send_keys(project)
        pro.send_keys(Keys.BACKSPACE)
        pro.send_keys(Keys.ENTER)

        #enter task
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_taskName"))).send_keys(task)

        #writing some description 
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_notes"))).send_keys(description)

        #click close
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-link']/span"))).click()
        log.Write_Info("Your TimeSheet have been submitted")

    def delete_add(self, date: str):
        """date_format: YY-MM-DD"""
        #Try click on 
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select date']"))).click()
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//td[@title='{}']".format(date)))).click()

        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[3]"))).click()
        WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        log.Write_Info("Submission deleted")