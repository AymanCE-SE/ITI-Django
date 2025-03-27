from django.urls import path
from .views import TraineeListCreateAPIView, TraineeUpdateDeleteAPIView

urlpatterns = [
    path('trainees/', TraineeListCreateAPIView.as_view(), name='trainee-list-create'),
    path('trainees/<int:pk>/', TraineeUpdateDeleteAPIView.as_view(), name='trainee-update-delete'),
]
