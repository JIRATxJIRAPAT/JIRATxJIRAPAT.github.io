from django.shortcuts import render ,get_object_or_404

from .models import course

# Create your views here.
def index(request):
    return render(request,"Courses/index.html",{
        "Course" : course.objects.all()
    })


def ShowCourse(request, course_code):
    info = get_object_or_404(course, pk = course_code)
    return render(request,"Courses/course_info.html" ,
    {"Course":info,
    })

