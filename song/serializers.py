from rest_framework import fields, serializers

from song.models import Song 


class SongSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Song
        fields = ('id', 'name', 'dateOfRelease', 'image', 'file', 'artist', 'created_by', 'image_url')

    def get_image_url(self, obj):
        return obj.image.url