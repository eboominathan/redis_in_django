from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from .models import Recipe


class RecipesView(ListView):
    """
    View to list all recipes.
    """
    queryset = Recipe.objects.all()
    context_object_name = 'recipes'
    template_name = 'recipes/recipes.html'
    

class RecipesDetailView(View):
    """
    View to handle the details of a single recipe.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("DetailsPage")    
