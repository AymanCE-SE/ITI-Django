from django.db import models



class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # active = models.BooleanField(default=True)
    course_duration = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True) 

    class Meta:
        db_table = "courses"
        ordering = ["id"]

    @classmethod
    def getCourseById(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def updateCourse(cls, id, name, description, active, course_duration):
        course = cls.getCourseById(id)
        course.name = name
        course.description = description
        course.active = active
        course.course_duration = course_duration
        course.save()
        return course
    
    @classmethod
    def getAllCourses(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name
