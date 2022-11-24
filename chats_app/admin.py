from django.contrib import admin
from .models import Chat, MemberChat, Message

# Register your models here.
admin.site.register(Chat)
admin.site.register(MemberChat)
admin.site.register(Message)
