from django.urls import path
from .views import CourseListView, CourseAddView, CourseUpdateView, CourseDeleteView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('add/', CourseAddView.as_view(), name='course_add'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('<int:pk>/detail/', CourseDetailView.as_view(), name='course_detail'),
]
