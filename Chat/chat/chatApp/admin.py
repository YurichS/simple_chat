from django.contrib import admin
from .models import User, Thread, Message

# Register your models here.
admin.site.register(User)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'updated', "messages_number")

    def messages_number(self, obj):
        return Message.objects.filter(thread=obj).count()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'text', 'thread', 'is_read')
