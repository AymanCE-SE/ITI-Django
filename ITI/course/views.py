from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Course
from .forms import CourseForm
from .serializers import CourseSerializer
from rest_framework import viewsets

class CourseAddView(View):
    template_name = 'forms/courseform.html'
    form_class = CourseForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')

            return redirect("course_list")
        return render(request, self.template_name, {'form': form})

class CourseUpdateView(View):
    template_name = 'forms/courseform.html'
    form_class = CourseForm

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = self.form_class(instance=course)
        return render(request, self.template_name, {'form': form, 'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = self.form_class(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')

            return redirect("course_list")
        return render(request, self.template_name, {'form': form, 'course': course})

class CourseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'courses'

class CourseDeleteView(View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        course.delete()
        messages.success(request, 'Course deleted successfully!')
        return redirect('course_list')
        
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courseDetail.html'
    context_object_name = 'course'



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer