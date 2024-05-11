from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_comments, name='read_comments'),
    path('comments/', views.add_record, name='add_comment'),
]
