import re, random
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient


# Obtain an admin key

adminClient = FaunaClient(secret="fnAEaN7AAdACUXdRhfTXLpP4Zaw9Gk3fL0kjULA3")
#
#retrieving data from fauna_database
#Retrieve Login datum
# email_list= []
# pass_list = []
#
#
# login_index = adminClient.query(
#     q.paginate(
#     q.match(q.index('loginIndex')))
#  )
# login_list = [login_index['data']]
# print()
#
#
#
# result = re.findall('\d+', str(login_list))
#
# for i in range(1,len(result)-2):
#     # print(f"Ref.ID - {i}: ", result[i])
#
#
#     login =adminClient.query(q.get(q.ref(q.collection("login"), result[i])))
#
#     detailsList = login['data']
#     email_list.append(detailsList['email'])
#     pass_list.append(detailsList['password'])
#
#
# userdata_list = list(zip(email_list, pass_list))
# random.shuffle(userdata_list)
# print(userdata_list[0][0])
# print(userdata_list[0][1])
#




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

updated_doc = adminClient.query(q.update( q.ref(q.collection("messages"), result[i]), { "data": {"facebook_posted": "N"} } ))
print(updated_doc)
