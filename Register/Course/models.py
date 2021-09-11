from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length = 5)
    course_name = models.CharField(max_length = 50)
    semester = models.SmallIntegerField()
    academic_year = models.CharField(max_length = 4)
    max_student = models.IntegerField()
    status = models.CharField(max_length = 5)
    
    def __str__(self):
        return f"{self.course_code} {self.course_name} {self.semester} {self.academic_year} {self.max_student} {self.status}"


class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_id = models.CharField(max_length = 10)
    grade = models.FloatField()
    years = models.CharField(max_length = 1)

    def __str__(self):
        return f"{self.student_name} {self.student_id} {self.grade} {self.years}"





