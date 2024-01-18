from django import forms
from .models import Student


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    msg = forms.CharField(widget=forms.Textarea, max_length=100)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "roll", "course"]
        widgets = {
            'name' : forms.TextInput(attrs={ "class" : "this is my class"})
        }