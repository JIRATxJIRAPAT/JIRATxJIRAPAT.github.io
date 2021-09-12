from django.contrib import admin

# Register your models here.

from .models import course,Student
class StudentUser(admin.ModelAdmin):
    filter_horizontal = ("enrollment",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_code","course_name","status")

admin.site.register(course,CourseAdmin)
admin.site.register(Student,StudentUser)

