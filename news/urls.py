from django.urls import path
from news import views
app_name='news'
urlpatterns = [
    path('',views.toIndex),
    path('index/',views.index,name="index"),
    path('list/',views.list,name='list'),
    path('article/',views.article,name='article'),

]