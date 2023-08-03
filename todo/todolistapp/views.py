from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def home(request):
    todo_queryset = Todo.objects.all()
    return render(request, 'home.html', {'todo' : todo_queryset})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title') #Request comes from html file form and url so we should check the request method before implementing data creation
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        Todo.objects.create(title = title, description = description, status = status)
        return redirect('home')
    content = {'method' : 'post' }
    return render(request, 'form.html', context=content)

def edit(request,pk):
    queryset = Todo.objects.get(id=pk)
    if request.method == "POST":
        queryset.title = request.POST.get('title')
        queryset.description = request.POST.get('description')
        queryset.status = request.POST.get('status')
        queryset.save()
        return redirect('home')

    return render(request, 'form.html', {'object':queryset , 'method': 'edit'})

def delete(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()
    return redirect('home')
