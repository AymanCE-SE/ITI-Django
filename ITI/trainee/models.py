from django.db import models
from django.core.validators import RegexValidator

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
    assigned_course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, null=True, to_field='id')
    image = models.ImageField(upload_to='images/%y/%m/%d', blank=True)

    class Meta:
        db_table = "trainees"
        ordering = ["id"]