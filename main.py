import pandas as pd
from config import chrome_options
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
session.timesheet()
session.submit(data["Start"][0], data["End"][0], data["Project"][0], data["Task"][0], data["Description"][0])
# session.delete_add("2022-10-08")
# time.sleep(20)