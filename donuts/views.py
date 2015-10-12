from django.shortcuts import render
from django.http import HttpResponse
from .models import Donut

def index(request):
    latest_donut_list = Donut.objects.order_by('-pub_date')[:5]
    context = {'latest_donut_list': latest_donut_list}
    return render(request, 'donuts/index.html', context)

def detail(request, donut_id):
    return HttpResponse("You're looking at donut %s." % donut_id)
