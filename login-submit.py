
######################################################
  
#########################################################

    

# #find login button
# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Terralogic Login']"))).click()

# #enter email
# email_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "identifierId")))
# email_input.send_keys(login_info[0])
# email_input.send_keys(Keys.ENTER)

# #enter password
# pw_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME, "password")))
# pw_input.send_keys(login_info[1])
# pw_input.send_keys(Keys.ENTER)
# '''Done login'''



driver.close()