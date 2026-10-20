from django.shortcuts import get_object_or_404, redirect, render
from .models import STATUS_CHOICES, Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description', ''),
            status=request.POST.get('status', 'new'),
            due_date=request.POST.get('due_date') or None,
        )
        return redirect('task_list')

    return render(request, 'webapp/task_form.html', {'status_choices': STATUS_CHOICES})
