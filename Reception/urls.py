from django.conf.urls import url
from django.urls import  include,path
from Reception import views
app_name="mml"
urlpatterns = [
    path('courses/',views.courses,name='courses'),
    path('members/',views.members,name='members'),
    path('layout/',views.layout,name='layout'),
    path('index/',views.index,name='index'),
    path('',views.toIndex),
    path('news/',include(('news.urls','news'),namespace='news')),

]