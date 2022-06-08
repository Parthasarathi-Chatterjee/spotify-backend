from django.contrib import admin
from accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'first_name', 'last_name', 'date_of_joining', 'is_active', 'created_at', 'modified_at', 'modified_at', 'deleted_at')

