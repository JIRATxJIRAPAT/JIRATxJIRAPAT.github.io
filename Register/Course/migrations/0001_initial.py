# Generated by Django 3.2.7 on 2021-09-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('semester', models.SmallIntegerField()),
                ('academic_year', models.CharField(max_length=4)),
                ('max_student', models.IntegerField()),
                ('status', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=10)),
                ('grade', models.FloatField()),
                ('years', models.CharField(max_length=1)),
            ],
        ),
    ]
