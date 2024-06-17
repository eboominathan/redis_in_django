from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from .models import Recipe
from django.core.cache import cache


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
        template_name = 'recipes/view.html'
        recipe_id = kwargs['pk']

        if cache.get(recipe_id):
            recipe = cache.get(recipe_id)
            print("Hit The Cache")
        else:
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                cache.set(recipe_id, recipe)
                print("Hit The DB")
            except Recipe.DoesNotExist:
                return HttpResponse("Recipe Does Not Exist")

        context = {'recipe': recipe}
        return render(request, template_name, context)
