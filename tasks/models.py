from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.CharField(max_length=250)

    # status=models.ForeignKey(
    # Status,
    # related_name="presentations",
    # on_delete=models.PROTECT,
    # )

    # assignee = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     related_name="tasks",
    #     on_delete=models.CASCADE,
    # )

    # project = models.ForeignKey(
    #     Project,
    #     related_name="tasks",
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Tasks"

class Project(models.Model):
    title = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.CharField(max_length=250)

    # team = models.ForeignKey(
    #     Team,
    #     related_name="Projects",
    #     on_delete=models.PROTECT,
    # )
    # author = models.ForeignKey(
    #     User,
    #     related_name = "Projects",
    #     on_delete=models.PROTECT
    # )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("due_date",)
        verbose_name_plural = "Projects"

class Status(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = "statuses"