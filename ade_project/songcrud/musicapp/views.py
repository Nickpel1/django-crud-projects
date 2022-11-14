from rest_framework.response import Response
from django.shortcuts import render
from .models import Song, Artiste, Lyric
from .serializers import SongSerializer, ArtisteSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def ArtisteList(request):
    if request.method == 'GET':
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data) 

        if serializer.is_valid() :  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
          
@api_view(['GET', 'PUT', 'DELETE'])
def ArtisteDetail(request, pk):
      try:
         artiste = Artiste.objects.get(pk=pk)
      except artiste.DoesNotExist: 
         return Response(status=404)  

      if request.method == 'GET': 
         serializer = ArtisteSerializer(artiste)
         return Response(serializer.data)
      elif request.method == 'PUT':
        serializer = ArtisteSerializer(artiste,data=request.data) 

        if serializer.is_valid() :  
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors, status=400) 
      elif request.method == 'DELETE':
            artiste.delete() 
            return Response(status=204) 

@api_view(['GET', 'POST'])
def SongList(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer =SongSerializer(song, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data) 

        if serializer.is_valid() :  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
          

@api_view(['GET', 'PUT', 'DELETE'])
def SongDetail(request, pk):
      try:
         song = Song.objects.get(pk=pk)
      except song.DoesNotExist: 
         return Response(status=404)  

      if request.method == 'GET': 
         serializer = SongSerializer(song)
         return Response(serializer.data)
      elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data) 

        if serializer.is_valid() :  
            serializer.save()
            return Response(serializer.data)
            return Response(serializers.errors, status=400) 
      elif request.method == 'DELETE':
            song.delete() 
            return Response(status=204)