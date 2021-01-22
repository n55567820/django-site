from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import _get_articles, _get_articles_by_id, _create_articles, _edit_articles_by_id, _del_articles_by_id
from .articles_form import create_articles_form, edit_articles_form
from .registerform import register_form

# Create your views here.

def index(request):
    articles = _get_articles()
    content = {"articles":articles}
    return render(request,"index.html",content)

def view_article(request,a_id):
    context = {"article":_get_articles_by_id(a_id)}
    return render(request,"show_articles.html",context)

def create_article(request):
    if request.method == "POST":
        _create_articles(request)
        return redirect("index")
    else:
        form = create_articles_form()
        context = {"form":form}
        return render(request,"create_articles.html",context)

def edit_article(request,a_id):
    if request.method == 'POST':
        _edit_articles_by_id(request, a_id)
        return redirect('index')
    else:
        form = edit_articles_form(a_id)
        context = {"form": form, "id": a_id}
        return render(request, "edit_articles.html", context)

def delete_article(request,a_id):
    _del_articles_by_id(a_id)
    return redirect("index")

def signin(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")
    else:
        return redirect("index")

def login(request):
    #Session.objects.all().delete()
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        auth_login(request,user)
        return redirect("index")
    else:
        return render(request,"login_fail.html")

def logout(request):
    auth_logout(request)
    return redirect("index")

def signup(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(request,username=new_user.username, password=request.POST['password1'])
            auth_login(request,user)
            return redirect("index")
        else:
            content = {'form':form}
            return render(request,"signup.html",content)
    else:
        form = register_form()
        content = {'form':form}
        return render(request, "signup.html", content)
