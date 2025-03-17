from django.urls import path
from . import views

app_name = "fields"
urlpatterns = [
    path('', views.read_comments, name='read_comments'),
    path('comments/', views.add_record, name='add_comment'),
]
