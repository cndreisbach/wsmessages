import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class BoopConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope['user']
        async_to_sync(self.channel_layer.group_add)(f"user-{self.user.pk}",
                                                    self.channel_name)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({'message': message}))

    def boop_create(self, event):
        self.send(text_data=json.dumps({
            'type': 'boop',
            'sender': event["sender"],
            'recipient': event["recipient"]
        }))
