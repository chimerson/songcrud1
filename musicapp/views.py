from ast import Try
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer

@csrf_exempt
def artist_list(request):
    """list all artists"""
    if request.method == 'GET':
        artists = Artiste.objects.all()
        serializer = ArtisteSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def song_list(request):
    """list all songs"""
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)  

@csrf_exempt
def song_detail(request, pk):
    """retrieve, update or delete a song"""
    try: 
        song =Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return HttpResponse(status=404)    

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400) 

    elif request.method == 'DELETE':
        song.delete()
        return HttpResponse(status=204)           
                




