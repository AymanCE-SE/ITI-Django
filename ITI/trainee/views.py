from django.shortcuts import render, redirect, get_object_or_404
from course.models import Course
from .models import Trainee
from .forms import TraineeForm
from django.views.generic import  ListView, DeleteView, DetailView
from django.views import View
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from .serializers import TraineeSerializer

class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee.html'
    context_object_name = 'trainees'

#CBVs for Template View
class TraineeAddView(View):
    template_name = 'traineeform.html'

    def get(self, request):
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses})

    def post(self, request):
        data = request.POST
        image = request.FILES.get('image')
        
        trainee = Trainee.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            age=data.get('age'),
            assigned_course_id=data.get('course_id'),
            image=image
        )
        messages.success(request, 'trainee added successfully!')


        return redirect('trainee_list')
    
#CBVs For Form View
class TraineeAddFormView(View):
    template_name = 'forms/traineeForm.html'  
    form_class = TraineeForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'trainee added successfully!')

            return redirect('trainee_list')
        return render(request, self.template_name, {'form': form})

class TraineeUpdateView(View):
    template_name = 'forms/traineeform.html'
    form_class = TraineeForm

    def get(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        form = self.form_class(instance=trainee)
        return render(request, self.template_name, {'form': form, 'trainee': trainee})

    def post(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=trainee)
        if form.is_valid():
            form.save()
            messages.success(request, 'trainee updated successfully!')
            return redirect("trainee_list")
        return render(request, self.template_name, {'form': form, 'trainee': trainee})


#delete in generic
class TraineeDeleteView(DeleteView):
    model = Trainee
    success_url = reverse_lazy('trainee_list')
    
    def form_valid(self, form):
        self.object.delete()
        messages.success(self.request, 'trainee deleted successfully!')
        return redirect(self.success_url)
        
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#Detail in generic
class TraineeDetailView(DetailView):
    model = Trainee
    template_name = 'traineeDetail.html'
    context_object_name = 'trainee'


class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

#Generic
# class TraineeCreateView(CreateView):
#     model = Trainee
#     fields = '__all__'
#     template_name = 'forms/traineeform.html'
#     success_url = '/trainees'





# def add_trainee(request):

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         age = int(request.POST.get('age'))
#         course_id = request.POST.get('course_id')
#         phone = request.POST.get('phone')
#         image = request.FILES.get('image')

#         Trainee.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             age=age,
#             phone=phone,
#             assigned_course_id=course_id,
#             image=image,
#         )
#         return redirect('trainee_list')
#     courses = Course.objects.all()
#     return render(request, 'traineeform.html', {'courses': courses})


# Create your views here.
# def add_trainee(request):
#     return render(request,'traineeform.html')
    # return HttpResponse("hello trainee")

# def getalltrainee(request):

#     return render(request,'trainee.html', {'trainees': Trainee.objects.all()})

# def update_trainee(request, trainee_id):
#     trainee = Trainee.objects.get(id=trainee_id)
#     if request.method == 'POST':
#         trainee.first_name = request.POST.get('first_name')
#         trainee.last_name = request.POST.get('last_name')
#         trainee.email = request.POST.get('email')
#         trainee.age = int(request.POST.get('age'))
#         trainee.phone = request.POST.get('phone')
#         trainee.assigned_course_id = request.POST.get('course_id')

#         new_image = request.FILES.get('image')
#         if new_image:
#             trainee.image = new_image
#         trainee.save()
#         return render(request, 'trainee.html', {'trainees': Trainee.objects.all()})
    
#     courses = Course.objects.all()
#     return render(request, 'traineeform.html', {'trainee': trainee, 'courses': courses})

# def delete_trainee(request, trainee_id):
#     trainee = Trainee.objects.get(id=trainee_id)
#     trainee.delete()
#     return render(request, 'trainee.html', {'trainees': Trainee.objects.all
# ()})
    
    
# def createTrainee(request):
#     form = TraineeForm()
#     if request.method == 'POST':
#         form = TraineeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('trainees')
#     return render(request, 'forms/traineeform.html', {'form': form})
