from django.urls import path
from .views import ArtisteList, ArtisteDetail, SongList, SongDetail


urlpatterns = [
    
   
    path('artiste/', ArtisteList),
    path('artiste/<int:pk>', ArtisteDetail),
    path('song/', SongList),
    path('song/<int:pk>', SongDetail)
    
    
]