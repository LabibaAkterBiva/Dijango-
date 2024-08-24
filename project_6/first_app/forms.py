from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta :
        model=StudentModel
        fields= "__all__"
        labels={
            'name':'Student Name',
            'roll':'Roll Number'
        }
        help_texts={
            'name':'Enter your Full Name',
            'roll':'Enter your Roll Number'
        }
        widgets={
            'name':forms.TextInput(),
            
        }
        error_messages={
            'name':{
                'required':'Please Enter Your Name'
            },
            'roll':{
                'required':'Please Enter Your Roll Number'
            }
        }
