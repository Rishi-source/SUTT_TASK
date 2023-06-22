from django.contrib import admin
from app.models import register_table,appointment
from ChatMessage.models import Message , Profile

# Register your models here.
admin.site.register(Message),
admin.site.register(Profile),


