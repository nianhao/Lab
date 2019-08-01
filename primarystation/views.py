from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def toIndex(request):
    return HttpResponseRedirect(reverse("pst:index"))
def index(request):
    return render(request,'pst/index.html',{})
def whisper(request):
    return render(request,'pst/whisper.html',{})
def leacots(request):
    return render(request,'pst/leacots.html',{})
def album(request):
    return render(request,'pst/album.html',{})
def me(request):
    return render(request,'pst/about.html',{})
def details(request):
    return render(request,'pst/details.html',{})
def base(request):
    return render(request,'pst/base.html',{})