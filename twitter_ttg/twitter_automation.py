import time, random

import userdata_fauna_database as ud
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
# for i in range(4):
random.shuffle(ud.userdata_list)
final_data = ud.userdata_list[0]

random.shuffle(ud.twitter_comments)


final_comment = ud.twitter_comments[0][2] #twitter_comments[0][0] - index no , [0][1] - Reg Id , [0][2] - Message
# print(final_comment)

driver = webdriver.Chrome(r"D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://twitter.com/")
driver.maximize_window()

#SignIn
sign_in = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]")
sign_in.click()

#LogIn
login_user = driver.find_element(By.CSS_SELECTOR,"input[name='text']")
login_user.send_keys(f"{final_data[0]}", Keys.ENTER)

#Printing the username logged in and the tuple of data set used
print("Username is :", final_data[0])
print(f"Data used is : ", final_data) #data[0] - email, data[1] - password , data[2] - mobile

#Checkpoint to check whether we include password first or mobile number first

if (len(driver.find_elements(By.XPATH, "//input[@name='text']"))) == 0:

    login_pass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_pass.send_keys(f"{final_data[1]}", Keys.ENTER)

    if len(driver.find_elements(By.XPATH, "//span[contains(text(),'Verify your identity by entering the phone number ')]")) == 1:
            driver.find_element(By.XPATH, "//input[@name='text']").send_keys(f"{final_data[2]}", Keys.ENTER)

else:
    login_mobile = driver.find_element(By.XPATH, "//input[@name='text']")
    login_mobile.send_keys(f"{final_data[2]}", Keys.ENTER)

    login_pass = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_pass.send_keys(f"{final_data[1]}", Keys.ENTER)

    if len(driver.find_elements(By.XPATH, "//span[contains(text(),'Verify your identity by entering the phone number ')]")) == 1:
            driver.find_element(By.XPATH, "//input[@name='text']").send_keys(f"{final_data[2]}", Keys.ENTER)

#posting the data taken from the database
post_box = driver.find_element(By.XPATH, "//div[@data-block='true']//div")
post_box.click()
post_box.send_keys(f"{final_comment}",Keys.CONTROL, Keys.ENTER)

# search = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Twitter']")
# search.send_keys("toptechguru",Keys.ENTER)

#reply_box = driver.find_elements(By.XPATH,"//div[contains(@aria-label,'Reply')]")
# for reply in reply_box:
#     reply.click()
#     comment_box = driver.find_element(By.CSS_SELECTOR,".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
#     comment_box.send_keys("This is a test", Keys.CONTROL, Keys.ENTER)
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(2)

account_menu = driver.find_element(By.XPATH,"//div[@aria-label='Account menu']")
account_menu.click()

account_logout = driver.find_element(By.XPATH,"//a[@href='/logout']")
account_logout.click()
logout_confirm = driver.find_element(By.XPATH,"//div[@dir='auto']//span//span[contains(text(),'Log out')]")
logout_confirm.click()
driver.quit()


print("Index no message from fauna database is : ", ud.twitter_comments[0][0])

#Ref id taken from data base
ref_id = ud.twitter_comments[0][1] #twitter comments holds pair of index val, Reg Id and twitter comment message in a tuple inside list.

print("Ref-id of message from fauna database is :", ref_id)



#Updating the post status to "Y"
updated_doc = ud.adminClient.query(ud.q.update(ud.q.ref (ud.q.collection("messages"), f"{ref_id}"), { "data": {"twitter_posted": "Y"} } ))
print("Successfully Posted and Status of the message changed to 'Y'")

