from django.shortcuts import render

# Create your views here.
# from __future__ import unicode_literals

from .models import ServiceDT
# Create your views here.


def home(request):
     return render(request,'home.html')

def ops(request):
     s_list = ServiceDT.objects.all()
     context = {'server_list': s_list}
     return render(request,'ops.html',context)

def dev(request):
     s_list = ServiceDT.objects.all()
     context = {'server_list': s_list}
     return render(request,'dev.html',context)