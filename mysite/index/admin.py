from django.contrib import admin
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'avatar', 'user', 'city')


admin.site.register(Profile, ProfileAdmin)
