from django.urls import path

from . import views

app_name="Course"
urlpatterns =[ 
    path('',views.index,name= "index"),
    path('<course_code>', views.ShowCourse ,name='Course')
]