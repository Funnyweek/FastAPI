from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'course']
    list_filter = ['course']
    search_fields = ['name', 'email']
