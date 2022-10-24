from django.shortcuts import render

# Create your views here.

def skills(request):
    d={"skill":'active'}
    return render(request,'edu/skills.html',d)
