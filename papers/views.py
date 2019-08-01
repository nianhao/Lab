from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def toIndex(request):
    return HttpResponseRedirect(reverse('papers:index'))
def index(request):
    return render(request,'papers/index.html',{})
