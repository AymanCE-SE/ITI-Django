from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def getallcourse(request):
    courses = Course.objects.all() 
    return render(request, 'course.html', context={'courses': courses}) 

def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name", "").strip()
        course_description = request.POST.get("course_description", "").strip()
        duration = request.POST.get("course_duration", 0)
        status = request.POST.get("status", False)

        if course_name: 
            Course.objects.create(
                name=course_name,
                description=course_description,
                course_duration=int(duration),
            )
            return redirect("course")  

    return render(request, "courseform.html")  

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course

def update_course(request, course_id):
    
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == "POST":
        course.name = request.POST.get("course_name", "").strip()
        course.description = request.POST.get("course_description", "").strip()
        course.course_duration = int(request.POST.get("course_duration", 0))
        course.status = request.POST.get("status", False)
        course.save()
        return redirect("course")

    return render(request, "courseform.html", {"course": course})  


from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from .forms import CourseForm

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect("course")

def createCourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course(
                name=form.cleaned_data['courseName'].strip(),
                description=form.cleaned_data['courseDescription'].strip(),
                course_duration=form.cleaned_data['courseDuration'],
                active=form.cleaned_data['active'],
            )
            course.save()
            return redirect("course")
    return render(request, "forms/courseform.html", {"form": form})
