from django.contrib import admin

from song.models import Rating, Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfRelease', 'image', 'file', 'created_by')


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'song', 'rating')

# admin.site.register(Name, NameAdmin)


