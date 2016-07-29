import time
import json
from slackclient import SlackClient





token = ""# found at https://api.slack.com/web#authentication
sc = SlackClient(token)

def handle(message):
	json_string=message
	obj = json.loads(json_string)
	# print(obj)
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


