# from django.db import models
#
# GRADES = (
#     (5.0, 'bardzo dobry'),
#     (4.5, 'dobry plus'),
#     (4.0, 'dobry'),
#     (3.5, 'dostateczny plus'),
#     (3.0, 'dostateczny'),
#     (2.0, 'niedostateczny')
# )
#
#
# class Department(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class Faculty(models.Model):
#     name = models.CharField(max_length=255)
#     department = models.OneToOneField(Department, on_delete=models.CASCADE)
#
#
# class Speciality(models.Model):
#     name = models.CharField(max_length=255)
#     faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)
#
#
# class Subject(models.Model):
#     name = models.CharField(max_length=255)
#     lecturer = models.CharField(max_length=255)
#     speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
#
#
# class Student(models.Model):
#     student_number = models.IntegerField(max_length=5, auto_created=True, unique=True)
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     faculty = models.ManyToManyField(Faculty)
#     speciality = models.OneToOneField(Speciality, on_delete=models.CASCADE)
#     grades = models.ManyToManyField(Subject, through='StudentGrades')
#
#
# class StudentGrades(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     grade = models.FloatField(choices=GRADES)
