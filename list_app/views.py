#pylint:disable=E1101

from django.shortcuts import render, redirect
#from django.http import HttpResponse
from list_app.models import TodoList
from list_app.forms import TaskForms
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request):
	if request.method == 'POST':
		form = TaskForms(request.POST or None)
		if form.is_valid():
			form.save(commit=False).manager = request.user
			form.save()
			messages.success(request,'New Task Added Successfully!')		
		return redirect('todolist')
	else:	
		#get all tasks from DB
		all_tasks = TodoList.objects.filter(manager=request.user)
		#adding paginator
		paginator = Paginator(all_tasks, 5)
		pg = request.GET.get('page')
		all_tasks = paginator.get_page(pg)
		
		return render(request, 'todolist.html', {'all_tasks': all_tasks})
	
def contact(request):
	
	context = {
	  'contact_text':'Welcome To Contact Us Page',
	  
	}
	return render(request, 'contact.html', context)
	
def index(request):
	
	context = {
	 	 'index_text':'Welcome To Home Page',	  
		   	}
	return render(request, 'index.html', context)


def about(request):
	
	context = {
	  'about_text':'Welcome To About Us Page',
	  
	}
	return render(request, 'about.html', context)

@login_required	
def delete_task(request, task_id):
	task = TodoList.objects.get(pk=task_id)
	if task.manager == request.user:
		task.delete()
	else:
		messages.error(request, ('Access Restricted, You\'re Not Allowed!'))
	return redirect('todolist')

@login_required
def complete_task(request, task_id):
	task = TodoList.objects.get(pk=task_id)
	if task.manager == request.user:
		task.done = True
		task.save()
	else:
		messages.error(request, ('Access Restricted, You\'re Not Allowed!'))
	return redirect('todolist')

@login_required
def pending_task(request, task_id):
	task = TodoList.objects.get(pk=task_id)
	if task.manager == request.user:
		task.done = False
		task.save()
	else:
		messages.error(request, ('Access Restricted, You\'re Not Allowed!'))
	return redirect('todolist')
	
@login_required
def edit_task(request, task_id):
	if request.method == 'POST':
		task = TodoList.objects.get(pk=task_id)
		form = TaskForms(request.POST or None, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request,'Your Task Has Been Edited Successfully!')		
	
		return redirect('todolist')
	else:	
		task_obj = TodoList.objects.get(pk=task_id)
		return render(request, 'edit.html', {'task_obj': task_obj})

	