import pandas as pd
from config import chrome_options
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
session = Timesheet(chrome_options)
session.get_url(url)
session.login(login_info)
time.sleep(10)
session.timesheet(data)
time.sleep(30)

