from django.urls import path

from . import views

urlpatterns = [
    path('trainees', views.getalltrainee, name='trainees'),
    path('add_trainee', views.add_trainee, name='add_trainee'),
    path('update/<int:trainee_id>', views.update_trainee, name='update'),
    path('trainees/delete/<int:trainee_id>/', views.delete_trainee, name='delete'),
    path('form/trainee', views.createTrainee, name='createTrainee'),
    
]