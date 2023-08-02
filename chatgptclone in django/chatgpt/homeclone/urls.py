from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chatgpt, name="chatgpt"),
    path('chatgpt1/', views.chatgpt1, name="chatgpt1"),


]
