import os
import asyncio
import websockets
from XSONotifications import XSOMessage, XSNotifier
XSNotifier = XSNotifier()
# Return cpu info
async def resources(websocket, path):
	async for message in websocket:
		input = message
		what = input.split(',')
		print(what)
		if what[0] == 'join':
			msg = XSOMessage()
			msg.messageType = 1
			msg.title = f"{what[1]} Joined [{what[2]}/{what[3]}]"
			msg.sourceApp = "XSNoti Python Test!"
			msg.opacity = 0.7
			XSNotifier.send_notification(msg)
			await websocket.send(f'{what[1]} Joined')
		elif what[0] == 'leave':
			msg = XSOMessage()
			msg.messageType = 1
			msg.title = f"{what[1]} Left [{what[2]}/{what[3]}]"
			msg.sourceApp = "XSNoti Python Test!"
			msg.opacity = 0.7
			XSNotifier.send_notification(msg)
			await websocket.send(f'{what[1]} Left')
		elif what[0] == 'worldload':
			msg = XSOMessage()
			msg.messageType = 1
			msg.title = "World Info"
			msg.content = f"<b>Session Name:</b> {what[1]} \n <b>State:</b> {what[2]} \n <b>Viewable:</b> {what[3]}"
			msg.sourceApp = "XSNoti Python Test!"
			msg.opacity = 0.7
			XSNotifier.send_notification(msg)
			await websocket.send(f'{what[1]} session joined')
		elif what[0] == 'worldstate':
			msg = XSOMessage()
			msg.messageType = 1
			msg.title = "World Info Changed"
			msg.content = f"<b>Session Name:</b> {what[1]} \n <b>State:</b> {what[2]} \n <b>Viewable:</b> {what[3]}"
			msg.sourceApp = "XSNoti Python Test!"
			msg.opacity = 0.7
			XSNotifier.send_notification(msg)
			await websocket.send(f'{what[1]} session changed')
		else:
			error = f"Invalid Query"
			await websocket.send(error)
			print('sent error response')

asyncio.get_event_loop().run_until_complete(websockets.serve(resources, '0.0.0.0', 5555))
asyncio.get_event_loop().run_forever()