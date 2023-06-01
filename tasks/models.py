from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    status= models.CharField(max_length=100, default="Not started")
    due_date = models.DateTimeField(null=True)
    completed_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.title