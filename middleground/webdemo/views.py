from django.shortcuts import render

# Create your views here.
def base(request):
    context={}
    return render(request, 'base.html', context)

def introduction(request):
    context={}
    return render(request, 'introduction.html', context)

def mission(request):
    context={}
    return render(request, 'mission.html', context)

def about(request):
    context={}
    return render(request, 'about.html', context)