from django.contrib import admin
from .models import Student, Subject, Question, Options, Exam, Point, Group

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam')

@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'it_correct', 'question')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'time')

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('subject', 'ball', 'student')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'students')





