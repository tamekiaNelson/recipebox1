from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from django.contrib.auth.models import User
from recipes.models import Recipe, Author
from recipes.forms import AuthordAdd, RecipeAdd


def index(request):
    html = 'index.html'
    recipes = Recipe.objects.all()
    return render(request, html, {'data': recipes})


def author(request, id):
    author_html = "author.html"
    authors = Author.objects.filter(id=id)
    recipes = Recipe.objects.filter(author=id)
    return render(request, author_html, {"data": authors, "recipes": recipes})


def recipe(request, id):
    recipe_html = "recipe.html"
    recipeList = Recipe.objects.filter(id=id)
    return render(request, recipe_html, {"data": recipeList})


def authoraddview(request):
    authoraddview_html = "generic_form.html"
    if request.method == "POST":
        form = AuthordAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data["name"],
                password=data["password"]
            )
            Author.objects.create(
                user=u,
                name=data["name"],
                bio=data.get("bio")
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthordAdd()
    return render(request, authoraddview_html, {form: form})


def recipeaddview(request):
    recipeaddview_html = "generic_form.html"
    if request.method == "POST":
        form = RecipeAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author=data["author"],
                title=data["title"],
                description=data["description"],
                instructions=data["instuctions"],
                post_time=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAdd()
    return render(request, recipeaddview_html, {form: form})
