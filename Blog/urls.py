from . import views
from django.urls import path

urlpatterns =[
    path("index/",views.index,name="index"),
    path('post/<str:post_id>/',views.detail,name="detail"),
]