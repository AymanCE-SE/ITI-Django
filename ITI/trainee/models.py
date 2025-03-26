from django.db import models
from django.core.validators import RegexValidator
from course.models import Course
from django.templatetags.static import static

# Create your models here
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField()
    phone = models.CharField(max_length=11, validators=[
        RegexValidator(
            regex=r'^01[0-2,5]{1}[0-9]{8}$',
            message='Phone number must be entered in the format: "01XXXXXXXXX". Up to 11 digits allowed.'
        )
    ])
    assigned_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='trainees')
    image = models.ImageField(upload_to='trainees/', null=True, blank=True)
    
    @classmethod
    def getTraineeById(cls,id):
        return cls.objects.get(id=id)
    
    @classmethod
    def updateTrainee(cls, id, first_name, last_name, email, age, phone, assigned_course_id, image):
        trainee = cls.getTraineeById(id)
        trainee.first_name = first_name
        trainee.last_name = last_name
        trainee.email = email
        trainee.age = age
        trainee.phone = phone
        trainee.assigned_course_id = assigned_course_id
        trainee.image = image
        trainee.save()
        return trainee
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return static('images/Default.png')
        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "trainees"
        ordering = ["id"]