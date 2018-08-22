#This is my first python project
#August 20, 2018 is when I started writing this file
#Download chromedriver from Chrome's wegsite and place it in /usr/local/bin

# this next block of code just opens the website in chrome
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
#driver.get ('http://www.theverge.com/')
myURL = ('https://my.uscis.gov/en/appointment/new?appointment%5Binternational%5D=false')
driver.get (myURL)
time.sleep(3)
from selenium.webdriver.common.by import By
# find element for zip code
Zip_Element = driver.find_element_by_id('appointments_appointment_zip')
# input zip code
Zip_Element.send_keys("11415")
# find search button and click it
search_button = driver.find_element_by_id('field_office_query')
search_button.click()
#wait 
time.sleep(3)
# find the nyc appointments section and click 
driver.find_element_by_id('NYC').click()
time.sleep (1)
# Checks for available appointments in NYC
nyc_appt = driver.find_element_by_xpath('//*[@id="NYC-notes"]/form/div/div[2]/div[1]')

nyc_appt.click()


#screenshot = driver.save_screenshot('my_screenshot.png')


# Support for sending email confirmation
'''
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("Snap41@gmail.com", "kartikurmish")
msg = "Hello, this is a script run confirmation!"
server.sendmail("Snap41@gmail.com", "kartiknath@gmail.com", msg)
server.quit()
'''
time.sleep(3)
# Close connection
driver.quit()
