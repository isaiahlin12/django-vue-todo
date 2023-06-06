from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    status= models.CharField(max_length=100, default="Not started")
    dueDate = models.DateTimeField(null=True, blank=True)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    