from django.shortcuts import render

# Create your views here.

def home(request):
    d={'home':'active'}
    return render(request,"core/home.html",d)

def contact(request):
    d={'contact':'active'}
    return render(request,'core/contact.html',d)
