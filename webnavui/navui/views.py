from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import LocationType, Location


def index(req):
    ctx = {}

    ctx['ltypes'] = [ { 'name': lt.name, 'locations': Location.objects.filter(location_type=lt, enabled=True).order_by('order') } for lt in LocationType.objects.filter(enabled=True).order_by('order') ]

    return render(req, 'navui/index.html', ctx)

@csrf_exempt
def navclick(req):
    pass
