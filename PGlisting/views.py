from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PG
# Create your views here.

class ListingPageView(ListView):
    model = PG
    template_name = '2ndpage.html'
    context_object_name = "PGs_list"

class PGDetailView(DetailView):
    model = PG
    template_name = '3rdpage.html'
