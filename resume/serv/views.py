from unicodedata import name
from django.shortcuts import render

# Create your views here.
def services(request):
    d={'services':"active"}
    return render(request,'serv/services.html',d)