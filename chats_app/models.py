from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    name = models.CharField(
        max_length=80,
        help_text='Название чата',
    )
    chat_members = models.ManyToManyField(
        User,
        through='MemberChat',
        through_fields=('chat', 'member'),
        help_text='Пользователи чата',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата создания чата',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Дата обновления чата',
    )

    def __str__(self):
        return f'{self.name} ({self.created_at})'


class Message(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text='Автор сообщения',
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text='Чат сообщения',
    )
    text = models.CharField(
        max_length=160,
        help_text='Текст сообщения',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата создания сообщения',
    )

    def __str__(self):
        return f'{self.author.username}: "{self.text}" ({self.created_at})'


class MemberChat(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='member_chats',
        help_text='Пользователь чата',
    )
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_members',
        help_text='Пользователь чата',
    )
    inviter = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='member_invites',
        help_text='Пригласитель',
    )
    invited_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата присоединения к чату',
    )

    def __str__(self):
        return f'{self.member.username} added to {self.chat.name} at {self.invited_at} '
