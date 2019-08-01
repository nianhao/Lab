from django.urls import  include,path
from papers import views
app_name="papers"
urlpatterns = [
    path('',views.toIndex),
    path('index/',views.index,name='index'),



]