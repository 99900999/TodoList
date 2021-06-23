from django import forms
from list_app.models import TodoList

class TaskForms(forms.ModelForm):
	class Meta:
		model = TodoList
		fields = ['task', 'done']
	