from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

