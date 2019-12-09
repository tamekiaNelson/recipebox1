from django.shortcuts import render
from recipes.models import Recipe, Author


def index(request):
    html = 'index.html'
    recipes = Recipe.objects.all()
    return render(request, html, {'data': recipes})


def author(request, id):
    author_html = "author.html"
    authors = Author.objects.filter(id=id)
    recipes = Recipe.objects.filter(authors=id)
    return render(request, author_html, {"data": authors, "recipes": recipes})


def recipe(request, id):
    recipe_html = "recipe.html"
    recipeList = Recipe.objects.filter(id=id)
    return render(request, recipe_html, {"data": recipeList})
