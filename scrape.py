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
time.sleep(5)

from selenium.webdriver.common.by import By

# find element for zip code
Zip_Element = driver.find_element_by_id('appointments_appointment_zip')
# input zip code
Zip_Element.send_keys("11415")
# find search button and click it
search_button = driver.find_element_by_id('field_office_query')
search_button.click()

#wait for 5 seconds

time.sleep(5)


# find the nyc appointments section and click 
driver.find_element_by_id('NYC').click()
driver.find_element_by_name('commit').click()


# driver.find_element('appointments_appointment_zip', 'TextArea').send_keys '11415'
# send keyboard actions, press `ctral+a` & `backspace`
# driver.find_element('appointments_appointment_zip', 'TextArea').send_keys [:contol, 'a'], :backspace
