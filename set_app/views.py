

from django.shortcuts import render
from set_app.models import *
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    todo = ToDo.objects.all()
    return render(request, 'index.html', {'todo': todo})

def create(request):
    if request.method == "POST":
        todo = ToDo.objects.all()
        new_todo = ToDo()
        new_todo.title = request.POST.get('title')
        new_todo.description = request.POST.get('description')
        tt = []
        for i in todo:
            tt.append(i.title)
        if new_todo.title in tt:
            return HttpResponseRedirect('/')
        else:
            new_todo.save()
            return HttpResponseRedirect('/')

def update(request, id):
    todo = ToDo.objects.get(id=id)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'index2.html', {'todo': todo})

# ----------  delete ---------

def delete_letter(request, id):
    todo = ToDo.objects.get(id=id)
    delete_todo=Delete()
    delete_todo.delete_title = todo.title
    delete_todo.delete_description = todo.description
    delete_todo.save()
    todo.delete()
    return HttpResponseRedirect('/')

def card(request):
    delete_todo = Delete.objects.all()
    return render(request, 'delete.html', {'delete_todo': delete_todo})

def delete_card(request, id):
    delete_todo = Delete.objects.get(id=id)
    delete_todo.delete()
    return HttpResponseRedirect('/card')


def w_card(request, id):
    delete_todo = Delete.objects.get(id=id)
    todo=ToDo()
    todo.title = delete_todo.delete_title
    todo.description = delete_todo.delete_description
    todo.save()
    delete_todo.delete()
    return HttpResponseRedirect('/card')
    

# -------- IZBRAN -------
def izbran(request):
    izbran_todo = Izbran.objects.all()
    return render(request, 'izbran.html', {'izbran_todo': izbran_todo})

def izbran_letter(request, id):
    todo = ToDo.objects.get(id=id)
    izbran_todo=Izbran()
    izbran_todo.izbran_title = todo.title
    izbran_todo.izbran_description = todo.description
    izbran_todo.save()
    return HttpResponseRedirect('/')

def izbran_delete(request, id):
    izbran_todo = Izbran.objects.get(id = id)
    izbran_todo.delete()
    return HttpResponseRedirect('/izbran')