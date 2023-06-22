from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User 
from app.models import register_table ,appointment
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from app.forms import appointment_form 
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.mail import EmailMessage
from google.oauth2 import id_token
from django.contrib.auth.models import User
from ChatMessage.serializers import MessageSerializer
from ChatMessage.models import Message , Profile
from rest_framework.parsers import JSONParser
from django.dispatch import receiver 
from django.contrib.auth.signals import user_logged_in, user_logged_out




# Create your views here.

def create_profile_for_new_user(sender, user, request, **kwargs):
    Profile.objects.create(user=user)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})





