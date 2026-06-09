from django.db import models

from course.models import Course

class Trainee(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 , null=False, blank=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    