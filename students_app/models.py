from django.db import models

# Create your models here.

# DB:
# courses: id, name, lecturer, description
# lecturers: id, name, email (unique), can teach


class Lecturers(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=45, unique=True)
    can_teach = models.CharField(max_length=30)


class Courses(models.Model):
    name = models.CharField(max_length=15, unique=True)
    lecturer = models.CharField(max_length=15)
    description = models.CharField(max_length=50)


class Students(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=45, unique=True)
    courses = models.ManyToManyField(Courses)

# makemigrations
# migrate
