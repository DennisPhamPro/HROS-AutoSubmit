from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from log import Log
import pathlib
import time

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
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_url(self, url : str):
        try:
            self.url = "https://"+ url
            log.Write_Info("Try navigating to {}...".format(self.url))
            self.driver.get(self.url)
            log.Write_Info("Done get URL")
        except:
            log.Write_Error("Cannot navigate to {} (maybe URL is not valid). Error detail is as below.".format(self.url))
            raise Exception("Something go wrong. Stop program now.")

    def login(self, login_info):
        try:
            #find login button
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[1]"))).click()
        except:
            log.Write_Error("Cannot click on login button.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            time.sleep(10)
            log.Write_Info("Try logging to HROS by TL account.")
            log.Write_Info("Typing your email!")    
            #enter email
            curr = self.driver.current_window_handle
            windows = self.driver.window_handles
            for window in windows:
                if window != curr:
                    self.driver.switch_to.window(window)
            email_input = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "identifierId")))
            email_input.send_keys(login_info[0])
            email_input.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
        except:
            log.Write_Error("Cannot type email (selector error). Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #enter password
            log.Write_Info("Typing your password!")    
            pw_input = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.NAME, "password")))
            pw_input.send_keys(login_info[1])
            pw_input.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
            self.driver.switch_to.window(curr)
        except:
            log.Write_Error("Cannot type password (Wrong email or selector error). Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='logo']")))
            log.Write_Info("Done logging!")
        except:
            log.Write_Error("Cannot logging to HROS. Wrong password.")
            raise Exception("Something go wrong. Stop program now.")
            

class Timesheet(HRMS):
    '''Timesheet functionality : Tasks, submissions,...'''
    def __init__(self, chrome_options):
        super().__init__(chrome_options)

    def timesheet(self):
        try:
            #nav and click timesheet
            log.Write_Info("Trying navigate to TimeSheet page")
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH,\
             "//span[contains(@class,'content')]//a[contains(@href,'sheet')]"))).click()
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH,\
             "//div[contains(@class,'AppFooter')]"))).click()   
            log.Write_Info("Done navigate to TimeSheet!")
        except:
            log.Write_Error("Cannot navigate to TimeSheet page. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

    def submit(self, date_start: str, date_end: str , project: str, task: str, description: str,\
     start_time: Optional[str] = "8:00 am" , end_time: Optional[str] = "5:00 pm"):
        """date_format: MM/DD/YY, time_format: 8:00 am"""


        log.Write_Info("Try adding TimeSheet")
        try:
            log.Write_Info("Try click on add task button.")
            #nav and click add task
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ant-btn')]/img"))).click()
            log.Write_Info("Done!")

        except:
            log.Write_Error("Cannot click on add task button. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #enter date
            log.Write_Info("Entering date ...")
            date = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_dates")))
            date.send_keys(date_start)
            end = self.driver.find_element(By.XPATH, "//input[@placeholder='End date']")
            end.send_keys(date_end)
            end.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
        except:
            log.Write_Error("Cannot enter start-end date. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #check time in
            log.Write_Info("Entering check in time ...")
            tin = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_startTime")))
            tin.send_keys(start_time)
            tin.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
        except:
            log.Write_Error("Cannot enter check in time. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #check time out
            log.Write_Info("Entering check out time ...")
            tout = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_endTime")))
            tout.send_keys(end_time)
            tout.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
        except:
            log.Write_Error("Cannot enter check out time. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #enter project
            log.Write_Info("Entering project ...")
            pro = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_projectId")))
            pro.send_keys(project)
            pro.send_keys(Keys.BACKSPACE)
            pro.send_keys(Keys.ENTER)
            log.Write_Info("Done!")
        except:
            log.Write_Error("Cannot enter project. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #enter task
            log.Write_Info("Entering task ...")
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_taskName"))).send_keys(task)
            log.Write_Info("Done!")
        except:    
            log.Write_Error("Cannot enter task. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #writing some description 
            log.Write_Info("Entering description ...")
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, "basic_tasks_0_notes"))).send_keys(description)
            log.Write_Info("Done!")
        except:    
            log.Write_Error("Cannot enter description. Error detail is as below.")
            raise Exception("Something go wrong. Stop program now.")

        try:
            #click submit
            log.Write_Info("submitting ...")
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            log.Write_Info("Your TimeSheet have been submitted (If not it is server fault not my code).")
        except:
            log.Write_Error("Cannot submit (selector error). Error detail is as below.")

    def delete_add(self, date: str):
        """date_format: YY-MM-DD"""
        #Try click on 
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select date']"))).click()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//td[@title='{}']".format(date)))).click()

        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//img[3]"))).click()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
