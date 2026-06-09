from django.db import models


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='For Testing')

    def __str__(self):
        return self.name
