from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render(request,'index.html')

def civic(request):
    return render(request, 'dashboard/civic.html')

def economic(request):
    return render(request,'dashboard/economic.html')

def safety(request):
    return render(request,'dashboard/safety.html')

def government(request):
    return render(request,'dashboard/governemnt.html')

def DataEntryForm(request):
    return render(request,'DataEntry/DataEntryForm.html')