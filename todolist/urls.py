
from django.contrib import admin
from django.urls import path, include
from list_app import views as list_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_app_view.index, name='index'),
    path('todolist/', include('list_app.urls')),
    path('accounts/', include('users_app.urls')),
    path('about', list_app_view.about, name='about'),
    path('contact', list_app_view.contact, name='contact'),
    
    
]
