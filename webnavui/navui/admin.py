from django.contrib import admin

from .models import *


class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', 'location_type', 'relay_no')
    list_filter = ('location_type',)
    search_fields = ('name', 'relay_no')


class NavigationActionAdmin(admin.ModelAdmin):

    list_display = ('ctime', 'location')
    list_filter = ('ctime', 'location')

admin.site.register(LocationType)
admin.site.register(Location, LocationAdmin)
admin.site.register(NavigationAction, NavigationActionAdmin)

