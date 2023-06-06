from django.urls import path 
from tasks import views

urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:id>', views.task_details),
]