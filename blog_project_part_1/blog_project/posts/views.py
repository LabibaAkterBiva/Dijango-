from django.shortcuts import render,redirect
from .import forms,models

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        add_post=forms.PostForm(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect('add_post')
    else:
        add_post=forms.PostForm()
        
    return render(request, 'add_post.html',{'form':add_post})

def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    edit_post=forms.PostForm(instance=post)

    if request.method == 'POST':
        edit_post=forms.PostForm(request.POST,instance=post)
        if edit_post.is_valid():
            edit_post.save()
            return redirect('home')
        
    return render(request, 'add_post.html',{'form':edit_post})
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
