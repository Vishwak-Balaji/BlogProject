from django.shortcuts import render
from django.http import HttpResponse, Http404
import logging

from Blog.models import Post


# Create your views here.
#
# static data which is not required
# posts = [
#     {"id": 1, "title": "Post 1", "content": "Content of post 1"},
#     {"id": 2, "title": "Post 2", "content": "Content of post 2"},
#     {"id": 3, "title": "Post 3", "content": "Content of post 3"},
#     {"id": 4, "title": "Post 4", "content": "Content of post 4"},
# ]
def index(request):
    blog_title = 'Latest posts'
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'blog_title': blog_title , 'posts':posts})


def detail(request,slug):
    # static data which is not rquired now
    # post = next((item for item in posts if item['id']== int(post_id)),None)
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Page does not exist")

    logger = logging.getLogger('Testing')
    logger.debug(f"Post variable is {post}")
    return render(request,'blog/detail.html',{'post':post})
