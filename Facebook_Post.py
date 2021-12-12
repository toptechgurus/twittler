import keyboard
from selenium import webdriver
import time
import openpyxl

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\atirumanur\Documents\chromedriver.exe")
driver.get(r"https://www.facebook.com/?stype=lo&jlou=AfefAFF_CGmgmOKtvoxd"
           r"-VftIBiMTQ7Yt1B0o4mPyqkMUcoPTf2__9y0vSJBaMR1aGoQlzm62x-v5NXY4zrPA19F685_HESvmg2dS2JDndABvQ&smuh=3467&lh"
           r"=Ac8QmNCITNDEE_bRRd8")
driver.maximize_window()
driver.implicitly_wait(5)
emailid = 'ttg-test1@protonmail.com'
passw = 'thisisatesT#22'
post = 'test post # 3'
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
time.sleep(5)
driver.implicitly_wait(5)
profie = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div['
                                      '1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div['
                                      '2]/div/div/div/div/span/span')
profie.click()
driver.implicitly_wait(5)
postb = driver.find_element_by_xpath('//span[contains(text(),"on your mind?")]')
postb.click()
driver.implicitly_wait(5)
post1 = driver.find_element_by_xpath('//div[@class="_1mf _1mj"]')
post1.click()
post1.send_keys(post)
driver.implicitly_wait(5)
postbtn = driver.find_element_by_xpath('//div[@aria-label="Post"]')
postbtn.click()

