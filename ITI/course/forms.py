from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'course_duration', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Course Description'}),
            'course_duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in weeks'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }