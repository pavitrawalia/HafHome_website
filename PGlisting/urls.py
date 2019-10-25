from django.urls import path
from .views import ListingPageView, PGDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pglist/', ListingPageView.as_view(), name='pglist'),
    path('pg/<int:pk>/', PGDetailView.as_view(), name='pg-details')
]
