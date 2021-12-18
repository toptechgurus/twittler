import keyboard
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\91787\PycharmProjects\selenium\driver\chromedriver.exe")
driver.get(r"https://www.facebook.com/?stype=lo&jlou=AfefAFF_CGmgmOKtvoxd"
           r"-VftIBiMTQ7Yt1B0o4mPyqkMUcoPTf2__9y0vSJBaMR1aGoQlzm62x-v5NXY4zrPA19F685_HESvmg2dS2JDndABvQ&smuh=3467&lh"
           r"=Ac8QmNCITNDEE_bRRd8")
driver.maximize_window()
driver.implicitly_wait(5)

# post = 'test post'
email = driver.find_element_by_xpath('//*[@id="email"]')
email.click()
email.send_keys(emailid)
driver.implicitly_wait(5)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.click()
password.send_keys(passw)
driver.implicitly_wait(5)
login = driver.find_element_by_xpath('//button[@name="login"]')
login.click()
time.sleep(5)
keyboard.press('escape')
keyboard.release('escape')