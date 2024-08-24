from django.shortcuts import render,redirect
from .import forms,models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        add_task=forms.TaskForm(request.POST)
        if add_task.is_valid():
            add_task.save()
            return redirect('homepage')
    else:
        add_task=forms.TaskForm()
    return render(request,'add_task.html', {'add_task':add_task})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    edit_task=forms.TaskForm(instance=task)
    if request.method == 'POST':
        edit_task=forms.TaskForm(request.POST, instance=task)
        if edit_task.is_valid():
            edit_task.save()
            return redirect('homepage')
    else:
        edit_task=forms.TaskForm(instance=task)
    return render(request,'add_task.html', {'add_task':edit_task})

def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('homepage')



     