from django.contrib.auth.models import User
from rest_framework import serializers

from chat.models import Message


class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['sender', 'recipient', 'timestamp', 'content']
        extra_kwargs = {
            "sender": {"read_only": True}
        }

    def validate(self, attrs):
        if self.context['request'].user == attrs['recipient']:
            raise serializers.ValidationError({"recipient": "Message can not be sent to the sender user."})
        attrs['sender'] = self.context['request'].user
        return attrs

