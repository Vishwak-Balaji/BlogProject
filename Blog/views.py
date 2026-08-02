from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog/index.html')
def detail(request,post_id):
    return render(request,'blog/detail.html')