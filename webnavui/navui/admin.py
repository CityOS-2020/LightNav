from django.contrib import admin

from .models import *


class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', 'location_type', 'relay_no', 'active')
    list_filter = ('location_type', 'active')
    search_fields = ('name', 'relay_no')


class NavigationActionAdmin(admin.ModelAdmin):

    list_display = ('ctime', 'location')
    list_filter = ('ctime', 'location')


class LocationTypeAdmin(admin.ModelAdmin):

    list_display = ('name', 'enabled', 'graph_link')

    def graph_link(self, obj):
        #return '<a href="/graph/lt?id=%d" target="_new">%s</a>' % (obj.id, obj.name)
        return """<a href="javascript:window.open('/graph/lt?id=%d', 'Event stats', 'toolbar=no,scrollbars=no,resizable=no,width=920,height=520')">%s</a>""" % (obj.id, obj.name)

    graph_link.allow_tags = True

admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(NavigationAction, NavigationActionAdmin)

