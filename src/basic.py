from slackclient import SlackClient

token = "xoxb-64602165441-JbOgUAdiTvYS1XM4HIjhbrBp"
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
        "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
        username='pybot', icon_emoji=':robot_face:'
)
