from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe, Author
from recipes.forms import AuthordAdd, RecipeAdd, LoginForm


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


@login_required
def authoraddview(request):
    authoraddview_html = "generic_form.html"
    if request.method == "POST":
        form = AuthordAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data.get("bio")
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthordAdd()
    return render(request, authoraddview_html, {'form': form})


@login_required
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
    return render(request, recipeaddview_html, {'form': form})


def login_view(request):
    loginview_html = "generic_form.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, loginview_html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
