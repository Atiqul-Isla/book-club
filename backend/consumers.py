import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'chat_%s' % self.pk
        
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        await self.accept()

    
    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester':tester,
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name 
        )
    
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message, 
            }
        )
    
    async def chatroom_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message, 
        }))
    pass