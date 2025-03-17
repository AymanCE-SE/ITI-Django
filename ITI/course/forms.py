from django import forms
from .models import Course

class CourseForm(forms.Form):
    courseName = forms.CharField(max_length=100, required=True , label="Course Name" , widget=forms.TextInput(attrs={'placeholder': 'Course Name'}))
    courseDescription = forms.CharField(max_length=1000, required=True , label="Course Description" , widget=forms.Textarea(attrs={'placeholder': 'Course Description'}))
    courseDuration = forms.IntegerField(required=True , label="Course Duration" , widget=forms.NumberInput(attrs={'placeholder': 'Course Duration'}))
    active = forms.BooleanField(required=False , label="Active" , widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    
    def clean_name(self):
        courseName= self.cleaned_data['courseName']
        #check if exists before 
        name_found = Course.objects.filter(name=courseName).exists()
        if name_found:
            raise forms.ValidationError("Course Name already exists")
        return courseName