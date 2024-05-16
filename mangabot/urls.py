from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.generate, name='generate'),
    path('', views.bot_page, name='bot_page')
]