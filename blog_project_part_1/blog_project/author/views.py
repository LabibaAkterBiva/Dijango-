from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_author(request):
    if request.method=='POST':                   #user post request kortese
        author=forms.AuthorForm(request.POST)        #user er post request er data akhana capture kora hosse
        if author.is_valid():                          #post kora data gulan valid ki na amra check kortesi
            author.save()                       #jodi valid hoy taile database a save korbe
            return redirect('add_author')             #sob thik thakle taka add_author url a pathaye dibo
    else:           #user normally website a gele blank data pabe 
         author=forms.AuthorForm()

   
    return render(request, 'add_author.html',{'form':author})