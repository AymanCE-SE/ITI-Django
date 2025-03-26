from django import forms
from django.core.exceptions import ValidationError
from .models import Trainee
from course.models import Course

class TraineeForm(forms.ModelForm):
    assigned_course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select a Course",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
        label="Course"
    )

    class Meta:
        model = Trainee
        fields = ['first_name', 'last_name', 'email', 'age', 'assigned_course', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'assigned_course': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.instance.pk is None: 
            if Trainee.objects.filter(email=email).exists():
                raise ValidationError("Email already exists")
        return email