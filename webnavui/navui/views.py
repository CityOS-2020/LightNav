from django.shortcuts import render

def index(req):
    ctx = {}
    return render(req, 'navui/index.html', ctx)
