from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render(request,'index.html')

def community(request):
    return render(request,'dashboard/community.html')

# The next two requests are the same, we could probably combine them into one function definition
def cultural(request):
    return render(request,'dashboard/recreationcultural.html')

def recreation(request):
    return render(request,'dashboard/recreationcultural.html')

def economic(request):
    return render(request,'dashboard/economic.html')

def environment(request):
    return render(request,'dashboard/environment.html')

def safety(request):
    return render(request,'dashboard/safety.html')

def transportation(request):
    return render(request,'dashboard/transportation.html')

def DataEntryForm(request):
    return render(request,'DataEntry/DataEntryForm.html')