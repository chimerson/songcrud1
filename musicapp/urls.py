from django.urls import path
from musicapp import views


urlpatterns = [
    path('musicapp/artists/', views.artist_list),
    path('musicapp/songs/', views.song_list),
    path('musicapp/songs/<int:pk>/', views.song_detail),
]