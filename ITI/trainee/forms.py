from django import forms
from django.core.exceptions import ValidationError
from .models import Trainee
from course.models import Course

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'course': forms.Select(attrs={'placeholder': 'Course'}),
            'track': forms.Select(attrs={'placeholder': 'Track'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def clean_name(self):
        name = self.cleaned_data['name']
        #check if exists before 
        name_found = Trainee.objects.filter(name=name).exists()
        if name_found:
            raise forms.ValidationError("Trainee Name already exists")
        return name