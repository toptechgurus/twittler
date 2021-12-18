import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Base:
    # def launch_browser(self):
    #     self.driver = webdriver.Chrome(executable_path=r"C:\Users\91787\PycharmProjects\selenium\driver\chromedriver.exe")
    #     self.driver.maximize_window()
    #     return self.driver
    # def Get_url(self,url,ref):
    #     ref.get(url)
    # def Find_element(self,xpath):
    #     self.element = self.driver.find_element_by_xpath(xpath)
    #     return self.element
    # def Setkeys(self,ref,text):
    #     ref.send_keys(text)
    # def Click(self,ref):
    #     ref.click()
    def keyboard(self,key):
        keyboard.press(key)
        keyboard.release(key)
    # def quit_browser(self):
    #     self.driver.quit()
    # def impwait(self,time):
    #     self.driver.implicitly_wait(time)
    # def Swapwindow(self,tab):
    #     self.driver.switch_to.window(tab)


