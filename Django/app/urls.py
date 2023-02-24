from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",Mydef,name='home'),
    path("crtldi/",MyCreateClass.as_view() ,name='CreatPost'),
    path('fbryt/<int:pk>/',UpdateView1.as_view(),name='yangilash'),
    path('<int:pk>/',DetailModel.as_view(),name='detail'),
]