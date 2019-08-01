from django.urls import  include,path
from primarystation import views
app_name="pst"
urlpatterns = [
    path('',views.toIndex),
    path('base/',views.base,name='base'),
    path('index/',views.index,name='index'),
    path('whisper/',views.whisper,name='whisper'),
    path('me/',views.me,name='me'),
    path('album/',views.album,name='album'),
    path('leacots/',views.leacots,name='leacots'),


]