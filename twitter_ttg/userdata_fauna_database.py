import re, random
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
# Obtain an admin key
adminClient = FaunaClient(secret="fnAEaN7AAdACUXdRhfTXLpP4Zaw9Gk3fL0kjULA3")

#retrieving data from fauna_database

#Retrieve Login datum
email_list= []
pass_list = []
mobile_list = []
comments_list = []
refId_list = []

login_index = adminClient.query(
    q.paginate(
    q.match(q.index('loginIndex')))
 )
login_list = [login_index['data']]
print() #new line

result_login = re.findall('\d+', str(login_list))

for i in range(1,len(result_login)):
    #print(f"Ref.ID - {i}: ", result[i])
    login =adminClient.query(q.get(q.ref(q.collection("login"), result_login[i])))

    detailsList = login['data']
    # print(detailsList)
    email_list.append(detailsList['email'])
    pass_list.append(detailsList['password'])
    mobile_list.append(detailsList['mobile_number'])

userdata_list = list(zip(email_list, pass_list, mobile_list))
# random.shuffle(userdata_list)


# Retrieve messages datum
messages_index = adminClient.query(
    q.paginate(
        q.match(q.index('messagesIndex')))
)

messages_list = [messages_index['data']]
result_msg = re.findall(r"\d+", str(messages_list))


for i in range(len(result_msg)):

    # print(f"Ref.ID - {i + 1}: ", result[i])
    # print(f"Ref.ID - {i + 1}: ", result[i])

    messages = adminClient.query(q.get(q.ref(q.collection("messages"), result_msg[i])))

    detailsList = messages['data']
    message_id = messages['data']['message_id']
    message_text = messages['data']['message_text']

    refId_list.append(result_msg[i])
    comments_list.append(message_text)

index_list=[]
for i in range(1,31):
    index_list.append(i)


twitter_comments = list(zip(index_list, refId_list, comments_list))
