from rest_framework import serializers
from .models import Artiste, Song

class ArtisteSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age', 'songs']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'date_released', 'likes']        
