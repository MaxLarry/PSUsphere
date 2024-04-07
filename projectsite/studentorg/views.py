from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    contextobject_name = 'home'
    template_name = "home.html"
# Create your views here.
