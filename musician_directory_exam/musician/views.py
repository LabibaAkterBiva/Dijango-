from django.shortcuts import render,redirect
from .import forms,models

# Create your views here.
def add_music(request):
    if request.method == 'POST':
        add_music=forms.MusicianForm(request.POST)
        if add_music.is_valid():
            add_music.save()
            return redirect('add_music')
    else:
        add_music=forms.MusicianForm()
        
    return render(request, 'add_music.html',{'form':add_music})

def edit_music(request,id):
    music=models.Musician.objects.get(pk=id)
    edit_music=forms.MusicianForm(instance=music)

    if request.method == 'POST':
        edit_music=forms.MusicianForm(request.POST,instance=music)
        if edit_music.is_valid():
            edit_music.save()
            return redirect('home')
        
    return render(request, 'add_music.html',{'form':edit_music})
def delete_music(request,id):
    musician=models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')

   

