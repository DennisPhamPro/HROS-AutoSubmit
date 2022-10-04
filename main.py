import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
##################################
from HRMS import HRMS
################################
url = 'terralogic.paxanimi.ai/login'
#################################
data = pd.read_csv('TimeSheet.csv')
week = 0
#################################
with open('info.txt', 'r', encoding= 'UTF-8') as file:
    info = file.read()
login_info = info.split()
#################################
session = HRMS()
session.get_url(url)
session.login(login_info)
time.sleep(20)
