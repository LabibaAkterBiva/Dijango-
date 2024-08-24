from django import forms 
from django.core import validators # Import the forms module from Django
# widgets
class contactForm(forms.Form):
    name = forms.CharField(label="User Name",initial='Rahim',help_text="total lenth must be within 10 characers",widget=forms.Textarea(attrs={'id':'text_area','class':'class1 class2','placeholder':'enter yiur name'}))
    file=forms.FileField()
    email = forms.EmailField(label="User Email")
    age=forms.CharField(label="Age",widget=forms.NumberInput)
    weight=forms.FloatField()
    balance=forms.DecimalField(label="Balance")
    check=forms.BooleanField(label="Check")
    birthday=forms.DateField(label="Birthday",widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(label="Appointment",widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    Choices=[('s','Small'),('m','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
    meal=[('p','paperoni'),('M','Mashroom'),('B','Beaf')]
    food=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     data = self.cleaned_data['name']
    #     if len(data)<10:
    #         raise forms.ValidationError("Name should be at least 10 characters long")        
    #     return data
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if "@gmail.com" not in valemail:
    #         raise forms.ValidationError("Please enter a valid gmail address")
    #     return valemail
    # def clean(self):
    #    cleaned_data=super().clean
    #    valname=self.cleaned_data['name']
    #    valemail=self.cleaned_data['email']
    #    if len(valname)<10:
    #      raise forms.ValidationError("Name should be at least 10 characters long")        
    #    if "@gmail.com" not in valemail:
    #      raise forms.ValidationError("Please enter a valid gmail address")

def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Name should be at least 10 characters long")        
    return value    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(20,message="message maximum charactot") , validators.MinLengthValidator(2,message="message at least 10")])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator("Enter a valid email")])
    text=forms.CharField(widget=forms.Textarea,validators=[len_check])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message="your age maximus 34") , validators.MinValueValidator(24,message="your age minimum 24")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='File must be pdf')])

class Passwordvalidation(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
      
      cleaned_data=super().clean()
      valpass=self.cleaned_data['password']
      valrepass=self.cleaned_data['repassword']
      valname=self.cleaned_data['name']
      if valpass!=valrepass:
          raise forms.ValidationError('Passwords do not match')
    
      if len(valname)<10:
           raise forms.ValidationError('Name should be at least 10 characters long')
      return cleaned_data