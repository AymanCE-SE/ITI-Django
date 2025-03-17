from django.urls import path
from .views import getallcourse, add_course, update_course, delete_course, createCourse

urlpatterns = [
    path('course', getallcourse, name='course'),
    path('add/', add_course, name='add_course'),
    path('update/<int:course_id>/', update_course, name='update_course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
    #from
    path('form/course',createCourse, name='createCourse'),
]
