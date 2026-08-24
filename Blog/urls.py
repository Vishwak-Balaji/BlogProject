from . import views
from django.urls import path

app_name ='blog'

urlpatterns =[
    path('', views.index, name='index'),
    path("index/",views.index,name="index"),
    path('post/<str:slug>/',views.detail,name="detail"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about, name="about"),

]