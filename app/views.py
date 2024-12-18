from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import formForm
from . models import items
def index(request):
    form=formForm()
    todo=items.objects.all()
    context = {
        "form":form,
        "todo":todo
    }
    if request.method=='POST':
        form=formForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "index.html",context)
def edit(request,id):
    todo=items.objects.get(id=id)
    form=formForm(instance=todo)
    context = {
        "form":form,
    }
    if request.method=='POST':
        form=formForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"edit.html",context)
def delete(request,id):
    todo=items.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect("/")