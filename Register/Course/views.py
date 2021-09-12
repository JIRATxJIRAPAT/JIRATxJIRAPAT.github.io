from django.shortcuts import render 

from .models import Course

# Create your views here.
def index(request):
    return render(request,"Course/index.html",{
        "Course" : Course.objects.all()
})


def ShowCourse(request, course_id):
    course = Course.objects.filter(course_id = course_id)
    return render(request,"Course/course.html" ,
    {"Course":course
})

