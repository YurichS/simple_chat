from rest_framework import serializers, viewsets
from .models import User, Thread, Message
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class CreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        thread_check = Thread.objects.filter(sender=validated_data['sender']).filter(
            receiver=validated_data['receiver'])
        if thread_check.exists():
            return thread_check
        thread = Thread(
            sender=validated_data['sender'],
            receiver=validated_data['receiver']
        )
        thread.save()
        return thread

    class Meta:
        model = Thread
        fields = ['sender', 'receiver']


class ThreadsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        message = Message(
            sender=validated_data['sender'],
            text=validated_data['text'],
            thread=validated_data['thread'],
        )
        message.save()
        return message

    class Meta:
        model = Message
        fields = ['sender', 'text', 'thread']


class MessagesInThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'text', 'is_read']
