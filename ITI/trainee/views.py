from django.shortcuts import render,redirect
from django.http import HttpResponse
from course.models import Course
from .models import Trainee
from .forms import TraineeForm
def add_trainee(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = int(request.POST.get('age'))
        course_id = request.POST.get('course_id')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')

        Trainee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            phone=phone,
            assigned_course_id=course_id,
            image=image,
        )
        return redirect('trainees' )
    courses = Course.objects.all()
    return render(request, 'traineeform.html', {'courses': courses})


# Create your views here.
# def add_trainee(request):
#     return render(request,'traineeform.html')
    # return HttpResponse("hello trainee")

def getalltrainee(request):

    return render(request,'trainee.html', {'trainees': Trainee.objects.all()})

def update_trainee(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    if request.method == 'POST':
        trainee.first_name = request.POST.get('first_name')
        trainee.last_name = request.POST.get('last_name')
        trainee.email = request.POST.get('email')
        trainee.age = int(request.POST.get('age'))
        trainee.phone = request.POST.get('phone')
        trainee.assigned_course_id = request.POST.get('course_id')

        new_image = request.FILES.get('image')
        if new_image:
            trainee.image = new_image
        trainee.save()
        return render(request, 'trainee.html', {'trainees': Trainee.objects.all()})
    
    courses = Course.objects.all()
    return render(request, 'traineeform.html', {'trainee': trainee, 'courses': courses})

def delete_trainee(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    trainee.delete()
    return render(request, 'trainee.html', {'trainees': Trainee.objects.all
()})
    
    
def createTrainee(request):
    form = TraineeForm()
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainees')
    return render(request, 'traineeform.html', {'form': form})
