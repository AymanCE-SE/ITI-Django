# Generated by Django 5.1.7 on 2025-03-12 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_image_course_course_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id']},
        ),
    ]
