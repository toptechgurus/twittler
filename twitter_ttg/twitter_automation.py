import time
from excel_data import user_data_excel as ud
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# chrome_path = "D:\Drivers\chromedriver_win32\chromedriver.exe"
#FireFox
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#Edge
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())

final_data = ud.userdata_list[1]
final_comment = ud.comments_list[0]

driver = webdriver.Chrome(executable_path=r"D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://twitter.com/")
driver.maximize_window()

sign_in = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]")
sign_in.click()

login_user = driver.find_element(By.CSS_SELECTOR,"input[name='text']")
login_user.send_keys(f"{final_data[0]}", Keys.ENTER)
print("Username is :", final_data[0])


if (len(driver.find_elements(By.XPATH, "//input[@name='text']"))) == 0:

    login_pass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_pass.send_keys(f"{final_data[1]}", Keys.ENTER)

else:
    login_mobile = driver.find_element(By.XPATH, "//input[@name='text']")
    login_mobile.send_keys(f"{final_data[2]}", Keys.ENTER)

    login_pass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_pass.send_keys(f"{final_data[1]}", Keys.ENTER)


search = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Twitter']")
search.send_keys("toptechguru",Keys.ENTER)

reply_box = driver.find_elements(By.XPATH,"//div[contains(@aria-label,'Reply')]")

for reply in reply_box:
    reply.click()
    comment_box = driver.find_element(By.CSS_SELECTOR,".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
    comment_box.send_keys(f"{final_comment}", Keys.CONTROL, Keys.ENTER)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


time.sleep(5)
account_menu = driver.find_element(By.XPATH,"//div[@aria-label='Account menu']")
account_menu.click()

account_logout = driver.find_element(By.XPATH,"//a[@href='/logout']")
account_logout.click()

logout_confirm = driver.find_element(By.XPATH,"//div[@dir='auto']//span//span[contains(text(),'Log out')]")
logout_confirm.click()
time.sleep(2)

print(driver.current_url)

time.sleep(2)
driver.quit()
