from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.conf import settings
from django.db.models import Q
# Create your views here.



class MyCreateClass(CreateView):
    model= Cinema
    template_name='create.html'
    fields=['title','author','text','img']


class UpdateView1(UpdateView):
    model = Cinema
    template_name = "update.html"
    fields=['title','author','text','img']




class DetailModel(DetailView):
    model=Cinema
    template_name='detail.html'

class Detail(DetailView):
    model = Cinema
    template_name='dtsh.html'

# class WeWe(ListView):
#     model = Cinema
#     template_name = 'home.html'
def Mydef(request):
    if 'q' in request.GET:
        q=request.GET['q']
        cinema = Cinema.objects.filter(title__icontains=q)
    else:
        q=None
        cinema = Cinema.objects.all()
        return render(request, 'home.html',{"Cinemas":cinema})