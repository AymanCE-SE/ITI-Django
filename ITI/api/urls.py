from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import TraineeViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'trainees', TraineeViewSet) 
router.register(r'courses', CourseViewSet)     

urlpatterns = [
    path('', include(router.urls)),
]
