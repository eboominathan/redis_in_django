from django.contrib import admin
from django.urls import path, include
from .views import RecipesView,RecipesDetailView


urlpatterns = [
    path('', RecipesView.as_view(),name='recipes'),    
    path('recipe/<int:pk>', RecipesDetailView.as_view(),name='recipe'),    
]
