import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from . import models
class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'chat_%s' % self.pk
        
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name 
        )
    
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        ## Find room object
        room = await database_sync_to_async(models.Room.objects.get)(id=self.pk)
        #  Create message
        chat = models.Message(
            message = message,
            user = self.scope['user'],
            room = room,
        )

        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message, 
                'username': username, 
            }
        )
    
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message, 
            'username': username, 
        }))
    pass
