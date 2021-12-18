import keyboard
from selenium import webdriver
import time
import re, random
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

# step 1 : code for getting random login from faunadb

# Obtain an admin key

adminClient = FaunaClient(secret="fnAEaN7AAdACUXdRhfTXLpP4Zaw9Gk3fL0kjULA3")
#
# retrieving data from fauna_database
# Retrieve Login data
email_list = []
pass_list = []

login_index = adminClient.query(
    q.paginate(
        q.match(q.index('loginIndex')))
)
login_list = [login_index['data']]
print()

result = re.findall('\d+', str(login_list))

for i in range(1, len(result) - 2):
    # print(f"Ref.ID - {i}: ", result[i])

    login = adminClient.query(q.get(q.ref(q.collection("login"), result[i])))

    detailsList = login['data']
    email_list.append(detailsList['email'])
    pass_list.append(detailsList['password'])

userdata_list = list(zip(email_list, pass_list))
random.shuffle(userdata_list)
print(userdata_list[0][0])
print(userdata_list[0][1])
emailid = userdata_list[0][0]
passw = userdata_list[0][1]

#  Step 2 : code for getting message which hasn't been posted in facebook

# Retrieve messages datum
messages_index = adminClient.query(
    q.paginate(
        q.match(q.index('messagesIndex')))
)

messages_list = [messages_index['data']]
# print(messages_list)
print()
result = re.findall(r"\d+", str(messages_list))
# print(re.findall(r"\d+", str(messages_list)))

for i in range(0, len(result)):
    print(f"Ref.ID - {i + 1}: ", result[i])

    messages = adminClient.query(q.get(q.ref(q.collection("messages"), result[i])))
    detailsList = messages['data']
    print(detailsList)
    postcheck = detailsList.get('facebook_posted')
    if postcheck == 'N':
        postmessage = detailsList.get('message_text')
        print(postmessage)
        break
    else:
        continue

#  Step 3 : code for posting message in facebook
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
time.sleep(10)
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
post1.send_keys(postmessage)
driver.implicitly_wait(5)
postbtn = driver.find_element_by_xpath('//div[@aria-label="Post"]')
postbtn.click()

# Step 4 : changing the status of the message in faunadb

updated_doc = adminClient.query(q.update( q.ref(q.collection("messages"), result[i]), { "data": {"facebook_posted": "Y"} } ))
print(updated_doc)