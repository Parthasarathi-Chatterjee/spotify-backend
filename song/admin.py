from django.contrib import admin

from song.models import Artist, Rating, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'dob', 'created_by')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfRelease', 'cover', 'created_by')


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'song', 'rating')

# admin.site.register(Name, NameAdmin)


