from django.db import models



class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    students = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name}"


class Exam(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=250)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Options(models.Model):
    name = models.CharField(max_length=250)
    it_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Point(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    ball = models.PositiveIntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
