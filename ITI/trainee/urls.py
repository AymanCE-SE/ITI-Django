from django.urls import path
from .views import (
    TraineeListView, 
    TraineeAddView,
    TraineeAddFormView,
    TraineeUpdateView, 
    TraineeDeleteView,
    TraineeDetailView
)

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee-list'),
    path('add/', TraineeAddView.as_view(), name='trainee-add'),
    path('add-form/', TraineeAddFormView.as_view(), name='trainee-add-form'),
    path('<int:pk>/update/', TraineeUpdateView.as_view(), name='trainee-update'),
    path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='trainee-delete'),
    path('<int:pk>/detail/', TraineeDetailView.as_view(), name='trainee-detail'),
]