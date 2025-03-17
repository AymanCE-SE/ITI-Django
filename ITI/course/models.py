from django.db import models

# Create your models here.

#This is Table and need to be added for DB
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    course_duration = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=True)

    class Meta:
        db_table = "courses"
        ordering = ["id"] 

