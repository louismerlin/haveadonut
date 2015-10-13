from django.shortcuts import render
from django.http import HttpResponse
from .models import Donut
from django.contrib.auth.models import User
from django.db.models import Count

def index(request):
    latest_donut_list = Donut.objects.order_by('-pub_date')[:10]
    best_user_list = User.objects.annotate(donut_count=Count('donut')).order_by('-donut_count')[:10]
    context = {
        'latest_donut_list': latest_donut_list,
        'best_user_list': best_user_list,
    }
    return render(request, 'donuts/index.html', context)
