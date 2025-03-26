from rest_framework import viewsets
from course.models import Course
from api.serializers.course_serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
