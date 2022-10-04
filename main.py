import pandas as pd
from config import chrome_options
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
session = HRMS(chrome_options)
session.get_url(url)
session.login(login_info)
time.sleep(10)