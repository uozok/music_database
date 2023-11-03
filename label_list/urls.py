from django.urls import path
from . import views

urlpatterns = [
    path('album_list/', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('news/', views.news_list, name='news_list'),  # news用
]

