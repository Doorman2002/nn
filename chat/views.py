# views.py
from django.shortcuts import render, redirect
from .models import Message
from signup.models import Signup

def chat(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')
    
    user = Signup.objects.get(id=user_id)

    if request.method == "POST":
        content = request.POST.get("message")
        if content:
            Message.objects.create(user=user, content=content)
        return redirect('/chat')  # redirect to avoid resubmitting form on refresh

    messages = Message.objects.filter(user=user).order_by('created_at')  # ensure ordering
    return render(request, 'chat.html', {'messages': messages, 'user': user})
