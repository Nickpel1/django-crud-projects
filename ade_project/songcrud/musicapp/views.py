from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Song, Artiste
from .serializers import SongSerializer, ArtisteSerializer

# Create your views here.

def index(request):
  return HttpResponse("Hello,this is my first django app")
  #views for song
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    #views for artiste
class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
         
