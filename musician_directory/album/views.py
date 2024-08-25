from django.shortcuts import render,redirect
from .import forms,models

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        add_album=forms.AlbumForm(request.POST)
        if add_album.is_valid():
            add_album.save()
            return redirect('home')
    else:
        add_album=forms.AlbumForm()
    return render(request, 'add_album.html', {'form': add_album})

def edit_album(request,id):
    edit_album=models.Album.objects.get(pk=id)
    if request.method == 'POST':
        edit_album=forms.AlbumForm(request.POST, instance=edit_album)
        if edit_album.is_valid():
            edit_album.save()
            return redirect('home')
    edit_album=forms.AlbumForm(instance=edit_album)

    return render(request, 'add_album.html', {'form':edit_album})

def delete_album(request,id):
    album=models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')