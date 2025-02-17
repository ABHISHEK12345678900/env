from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['uid', 'todo_title', 'todo_description', 'is_done']

admin.site.register(Todo, TodoAdmin)
