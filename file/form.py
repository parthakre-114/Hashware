from django import forms
from .models import Member,Learn,Akshada,Mohan,Fil

class UserInputForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname','email','password']

class learninput(forms.ModelForm):
    class Meta:
        model = Learn
        fields = ['name', 'email','number','courses','gender']        
 

class Moha(forms.ModelForm):
    class Meta:
        model = Mohan
        fields=['id','name']



class Akshada(forms.ModelForm):
    class Meta:
        model = Akshada
        fields = ['aname','aemail','aissue','aremark','aservice']       


class Filf(forms.ModelForm):
    class Meta:
        model = Fil
        fields = ['file']        