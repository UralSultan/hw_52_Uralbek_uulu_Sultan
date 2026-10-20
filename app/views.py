from django.shortcuts import get_object_or_404, redirect, render
from .models import STATUS_CHOICES, Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})

