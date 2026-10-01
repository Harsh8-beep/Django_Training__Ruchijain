from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cgpa', 'iq', 'profile_score') 
# Register your models here.
