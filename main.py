import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import chromedriver_autoinstaller
import time
# import logging 
##################################
from HRMS import Timesheet
################################
url = 'terralogic.paxanimi.ai/login'
#################################
data = pd.read_csv('TimeSheet.csv')

#################################
with open('info.txt', 'r', encoding= 'UTF-8') as file:
    info = file.read()
login_info = info.split()
#################################
session = Timesheet()
session.get_url(url)
print("Get URL DONE")
session.login(login_info)
print("Login DONE")
time.sleep(10)
session.timesheet(data)
time.sleep(20)
