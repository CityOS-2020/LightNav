import json
import time
import threading
import datetime

import qrcode

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Min, Max, Avg

from .models import LocationType, Location, NavigationAction



def index(req):
    ctx = {}
    ctx['ltypes'] = [ { 'name': lt.name, 'locations': Location.objects.filter(location_type=lt, enabled=True).order_by('order') } for lt in LocationType.objects.filter(enabled=True).order_by('order') ]
    return render(req, 'navui/index.html', ctx)


@csrf_exempt
def navclick(req):
    l = Location.objects.get(id=int(req.POST['lid']))

    if l.active:
        print("Already active %d" % l.relay_no)
        return JsonResponse({ 'ok': True, 'error': "Already lit" })

    na = NavigationAction(location=l)
    na.save()
    l.active = True
    l.save()

    l.turn_on_relay()

    t = threading.Thread(target=location_display_expiry_thread, args=(l,))
    t.daemon = True
    t.start()

    resp = { 'ok': True, 'lid': l.id, 'na': na.id, 'img': None }

    print(l.map_url)
    if l.map_url:
        img = qrcode.make(l.map_url)
        img.save('/home/pi/LightNav/webnavui/static/navui/%d.png' % l.id)
        resp['img'] = '%d.png' % l.id

    return JsonResponse(resp)


def usage_graph(req):
    ctx = {}
    ltid = int(req.GET['id'])
    evlist = [ date_clamp(x.ctime) for x in NavigationAction.objects.filter(location__location_type_id = ltid) ]
    ctx['evlist'] = evlist
    return render(req, 'navui/usage_graph.html', ctx)


def location_display_expiry_thread(l):
    print("Countdown of %d seconds to turn off relay %d" % (l.display_seconds, l.relay_no))
    try:
        time.sleep(l.display_seconds)
    finally:
        l.turn_off_relay()
        l.refresh_from_db()
        l.active = False
        l.save()


def unix_d(d):
    return time.mktime(d.timetuple())

def date_clamp(d):
    return -(unix_d(datetime.datetime.now()) - unix_d(d)) / 3600 

