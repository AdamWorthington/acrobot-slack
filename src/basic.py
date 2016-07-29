import time
import json
import base64
from slackclient import SlackClient




token_64 = "eG94Yi02NDYwMjE2NTQ0MS1OeWhqRjFvcWxGUW5JTENLQ0dVZVV2UUwK" #jank for now
token = base64.b64decode(token_64)
token=token.strip('\n')
sc = SlackClient(token)

def handle(message):
	json_string=message
	# obj = json.loads(json_string)
	print(json_string)
	# if obj == 'yolo':
	# 	sc.api_call(
	# 		"chat.postMessage", channel="#general", text="fuck your yolo",
	# 		username='pybot'
	# 		)

if sc.rtm_connect():
	while True:
		handle(sc.rtm_read())
		time.sleep(1)
else:
	print "Connection Failed, invalid token?"


