import json

from channels.generic.websocket import AsyncWebsocketConsumer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'comments'
        self.room_group_name = 'comments_group'

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
        comment = text_data_json['comment']

        # Включите все необходимые поля в отправляемых данных
        comment_data = {
            'username': comment['username'],
            'text': comment['text'],
            'created_at': comment['created_at'],
        }

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'comment_message',
                'comment': comment_data
            }
        )

    async def comment_message(self, event):
        comment = event['comment']

        await self.send(text_data=json.dumps({
            'comment': comment
        }))
