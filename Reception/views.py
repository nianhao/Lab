from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    #return HttpResponse("hello world")
    return render(request,"mml/index.html",{})
def toIndex(request):
    return HttpResponseRedirect(reverse("mml:index"))
def members(requset):
    return render(requset,'mml/members.html',{})
def courses(request):
    return render(request,'mml/courses.html',{})
def services(request):
    return render(request,'mml/services.html',{})
def icons(request):
    return render(request,'mml/icons.html',{})
def mail(request):
    return render(request,'mml/mail.html',{})
def typography(request):
    return render(request,'mml/typography.html',{})
def layout(request):
    return render(request, 'mml/../templates/layout.html', {})
def news(request):
    return render(request,'mml/news.html',{})