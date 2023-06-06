from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime
from .serializers import TaskSerializer
from .models import Task

@csrf_exempt
def tasks(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST': 
        data = JSONParser().parse(request)


        dueDate = None
        if data['dueDate']:
            dueDate = datetime.strptime(data['dueDate'], '%m/%d/%Y %H:%M')
        
        # completed_on = None
        # if data['completedOn']:
        #     completedOn=datetime.strptime(data['completedOn'], '%m/%d/%y %H:%M')

        TaskObj = Task(
            title = data['title'],
            status = data['status'],
            dueDate = dueDate,
            completed_on = None
        )
        print(data)
        TaskObj.save()
        return JsonResponse({'message': 'success!'}, status=200)
    
@csrf_exempt
def task_details(request, id):

    if request.method=='GET':
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, many=False) 

        return JsonResponse(serializer.data, safe=False)
    
    # elif request.method == 'PUT': 
    #     data = JSONParser().parse(request)
        
    #     TaskObj = Task.objects.get(id=id)

    #     TaskObj.dueDate = 
    #     TaskObj.completed_on = 

    #     return JsonResponse({'message': 'success!'}, status=200)
    
    elif request.method=='DELETE':
        task = Task.objects.filter(id=id).delete()
        return JsonResponse({"deleted": task})

def main (request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())