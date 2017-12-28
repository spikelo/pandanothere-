from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Username,Router
from django.views.generic import CreateView , DetailView , UpdateView
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
class Test(generic.ListView):
    model = Router
    template_name = 'test.html'
# Create your views here.
