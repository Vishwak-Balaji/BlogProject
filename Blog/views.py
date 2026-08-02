from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    blog_title = 'Latest posts'
    return render(request,'blog/index.html',{'blog_title': blog_title})
def detail(request,post_id):
    return render(request,'blog/detail.html')