from .serializers import SignUpSerializer, CreateSerializer, ThreadsListSerializer, CreateMessageSerializer, \
    MessagesInThreadSerializer
from .models import Thread, Message
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.db.models import Q
from django.utils.timezone import now


# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "user created successfully"})


class SignInView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"message": "Invalid email or password"})
        return Response({"message": "Login successfully"})


class CreateView(generics.GenericAPIView):
    lookup_field = 'username'

    def post(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Thread has been created"})
        return Response({"Error": serializer.errors})


class DeleteThreadView(generics.GenericAPIView):
    def post(self, thread_id):
        thread = Thread.objects.get(id=thread_id)
        thread.delete()
        return Response({"message": "Thread delete successfully"})


class ThreadsListView(generics.ListAPIView):
    serializer_class = ThreadsListSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Thread.objects.filter(Q(sender=user_id) | Q(receiver=user_id))


class CreateMessageView(generics.GenericAPIView):
    def post(self, request):
        serializer = CreateMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            thread = Thread.objects.get(id=request.data['thread'])
            thread.updated = now()
            thread.save()
            return Response({"message": "Message sent"})
        return Response({"Error": serializer.errors})


class MessagesInThreadView(generics.ListAPIView):
    serializer_class = MessagesInThreadSerializer

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Message.objects.filter(thread=thread_id)


class MessageReadView(generics.GenericAPIView):
    def post(self, request, message_id):
        message = Message.objects.get(id=message_id)
        message.is_read = True
        message.save()
        return Response({"sender": message.sender.email, "text": message.text})


class UnreadMessageNumberView(generics.GenericAPIView):
    def get(self, request, user_id):
        threads = Thread.objects.filter(Q(sender=user_id) | Q(receiver=user_id)).values_list('id', flat=True)
        number = 0
        for thread in threads:
            count = Message.objects.filter(Q(thread=thread) & Q(is_read=False)).exclude(sender=user_id).count()
            number += count
        return Response({"Number of unread messages": number})
