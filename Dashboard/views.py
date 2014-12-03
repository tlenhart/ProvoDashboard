from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')

def community(request):
    return render_to_response('dashboard/community.html')

# The next two requests are the same, we could probably combine them into one function definition
def cultural(request):
    return render_to_response('dashboard/recreationcultural.html')

def recreation(request):
    return render_to_response('dashboard/recreationcultural.html')

def economic(request):
    return render_to_response('dashboard/economic.html')

def environment(request):
    return render_to_response('dashboard/environment.html')

def safety(request):
    return render_to_response('dashboard/safety.html')

def transportation(request):
    return render_to_response('dashboard/transportation.html')

def inputpage(request):
    return render_to_response('dashboard/inputpage.html')