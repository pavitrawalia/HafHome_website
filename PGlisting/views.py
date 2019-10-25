from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import PG
# Create your views here.

class HomePageView(TemplateView):
    template_name = "1stpage.html"

class ListingPageView(ListView):
    model = PG
    template_name = '2ndpage.html'
    context_object_name = "PGs_list"

class PGDetailView(DetailView):
    model = PG
    template_name = '3rdpage.html'
