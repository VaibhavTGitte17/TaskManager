from django.contrib import admin

from .models import *

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")
    
#Register model

admin.site.register(Todo, TodoAdmin)
