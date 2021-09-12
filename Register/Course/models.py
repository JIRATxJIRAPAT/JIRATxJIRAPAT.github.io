from django.db import models

# Create your models here.
class course(models.Model):
    course_code = models.CharField(max_length = 5 ,primary_key = True)
    course_name = models.CharField(max_length = 50)
    semester = models.SmallIntegerField()
    academic_year = models.CharField(max_length = 4)
    max_student = models.IntegerField()
    status = models.CharField(max_length = 20)
    
    def __str__(self):
        return f"{self.course_code}"


class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_id = models.CharField(max_length = 10)
    grade = models.FloatField()
    years = models.CharField(max_length = 1)
    enrollment = models.ManyToManyField(course,blank = True)

    def __str__(self):
        return f"{self.student_id}: {self.student_name}"





