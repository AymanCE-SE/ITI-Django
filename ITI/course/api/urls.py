from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, update_course

router = DefaultRouter()
router.register(r'', CourseViewSet) 

urlpatterns = [
    path('', include(router.urls)),  
    path('<int:pk>/update/', update_course, name='course-update-fbv'), 
]
