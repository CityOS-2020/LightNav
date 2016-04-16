from django.db import models

class LocationType(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    location_type = models.ForeignKey(LocationType)
    name = models.CharField(max_length=15)
    relay_no = models.IntegerField(default=4)
    map_url = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class NavigationAction(models.Model):
    location = models.ForeignKey(Location)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location.name

