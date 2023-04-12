from rest_framework import fields, serializers

from artist.models import Artist



class ArtistSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'dob', 'created_by', 'image_url')

    def get_image_url(self, obj):
        return obj.image.url