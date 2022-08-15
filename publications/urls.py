from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('years/<str:year>/', views.year_wise_publications, name = 'year_wise_publications'),
    path('details/<str:id>/', views.details, name = 'details'),
    path('category/<str:document_type>/', views.category, name = 'category'),
    path('search/', views.search, name = 'search'),
]
