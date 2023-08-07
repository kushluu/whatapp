from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class MySysncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('connected',event)
        print("channel layer", self.channel_layer)
        print("channel layer", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'programmers',
            self.channel_name
        )
        self.send({
            'type' : 'websocket.accept'
        })


    def websocket_receive(self,event):
        print(event['text'])
        async_to_sync(self.channel_layer.group_send)(
            'programmers',
            {
                "type":'chat.message',
                'message':event['text']
            }
        )

    def websocket_disconnect(self,event):
        print('disconnected')
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()
    
    def chat_message(self,event):
        self.send({
            'type':"websocket.send",
            'text':event['message']
        })


class MyAsysncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connected',event)
        await self.send({
            'type' : 'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('received',event)
        print(event['text'])
        await self.send({
            'type' : 'websocket.send',
            'text' : str(event['text']+"amg"),
            'sender' : str(event['text']+"amg")
        })

    async def websocket_disconnect(self,event):
        print('disconnected')
        raise StopConsumer()


# consumers.py


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send(text_data=json.dumps({'message': message}))


# consumers.py

# import asyncio
# import json

# from channels.generic.websocket import AsyncWebsocketConsumer

# class MyWebSocketConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']

#         # Do something with the received message
#         response = {
#             'message': f'Received: {message}',
#         }

#         await self.send(text_data=json.dumps(response))

