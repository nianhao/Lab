from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

app_name="news"
def toIndex(request):
    return HttpResponseRedirect(reverse("news:index"))
def index(request):
    return render(request,'news/index.html',{})
def list(request):
    return render(request,'news/list.html')
def article(request):
    return render(request,'news/article.html')