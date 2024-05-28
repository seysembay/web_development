from django.contrib import admin
from .models import Course, CourseRun, Lesson, Enrollment, Homework, HomeworkSubmission

admin.site.register(Course)
admin.site.register(CourseRun)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Homework)
admin.site.register(HomeworkSubmission)
