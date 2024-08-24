from django.shortcuts import render
import  datetime
def home(request):
    d = {'author':'Lbiba','val':'' ,'age':50,'birthday':datetime.datetime.now(),'lst':['python','is','easy'],'v':"January - February - March" ,
         
         'courses':[
        {
            'title':'Python Basics',
            'id': 1,
            'instructor':'John Doe'
        },
        {
            'title':'Django Basics',
            'id': 2,
            'instructor':'Jane Smith'
        },
        {
            'title':'Web Development',
            'id': 3,
            'instructor':'Mark Brown'
        }
    ]
         }
    return render(request, 'home.html',d)

# Create your views here.
