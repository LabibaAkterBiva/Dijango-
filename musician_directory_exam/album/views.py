from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .import forms,models
from django.shortcuts import render
from .models import Album
from .forms import AlbumForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         add_album=forms.AlbumForm(request.POST)
#         if add_album.is_valid():
#             add_album.save()
#             return redirect('home')
#     else:
#         add_album=forms.AlbumForm()
#     return render(request, 'add_album.html', {'form': add_album})
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name="add_album.html"
    success_url = reverse_lazy('add_album')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Album'
        return context

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Album'
        return context
def edit_album(request,id):
    edit_album=models.Album.objects.get(pk=id)
    if request.method == 'POST':
        edit_album=forms.AlbumForm(request.POST, instance=edit_album)
        if edit_album.is_valid():
            edit_album.save()
            return redirect('home')
    edit_album=forms.AlbumForm(instance=edit_album)

    return render(request, 'add_album.html', {'form':edit_album})
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Album'
        return context
    
def delete_album(request,id):
    album=models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')
@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'