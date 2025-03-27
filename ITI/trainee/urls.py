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
    path('', TraineeListView.as_view(), name='trainee_list'),
    path('add/', TraineeAddView.as_view(), name='trainee_add'),
    path('add-form/', TraineeAddFormView.as_view(), name='trainee_add-form'),
    path('<int:pk>/update/', TraineeUpdateView.as_view(), name='trainee_update'),
    path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='trainee_delete'),
    path('<int:pk>/detail/', TraineeDetailView.as_view(), name='trainee_detail'),
]