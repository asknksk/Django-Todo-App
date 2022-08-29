from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo   
from .forms import TodoForm
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, "todoApp/home.html", context)

def todo_create(request):
    form = TodoForm()

    context = {
        "form" : form
    }
    return render(request, "todoApp/todo_add.html", context)