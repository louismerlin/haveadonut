from django.shortcuts import render
from django.http import HttpResponse
from .models import Donut, Chat
from django.db.models import Count

def index(request):
    latest_donut_list = Donut.objects.order_by('-pub_date')[:10]
    best_chat_list = Chat.objects.annotate(donut_count=Count('donut')).order_by('-donut_count')[:10]
    context = {
        'latest_donut_list': latest_donut_list,
        'best_user_list': best_chat_list,
    }
    return render(request, 'donuts/index.html', context)
