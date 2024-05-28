from django.db import models
from django.utils import timezone
from User.models import CustomUser


class Course(models.Model):
    DoesNotExist = None
    DURATION_UNIT_CHOICES = (
        ('weeks', 'недель'),
        ('months', 'месяцев'),
        ('years', 'лет'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField()
    duration = models.IntegerField()
    duration_unit = models.CharField(choices=DURATION_UNIT_CHOICES, default='months')
    icon_link = models.CharField(null=True)

    def __str__(self):
        return self.name


class CourseRun(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.course.name} ({self.id})"


class Lesson(models.Model):
    course = models.ForeignKey(CourseRun, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    start = models.DateTimeField(default=timezone.now)
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, limit_choices_to={'role_id': 1})

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT, limit_choices_to={'role_id': 2})
    course_run = models.ForeignKey(CourseRun, on_delete=models.PROTECT)


class Homework(models.Model):
    lesson = models.OneToOneField(Lesson, related_name='homeworks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class HomeworkSubmission(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Отправлен на проверку'),
        ('returned', 'Возвращен на доработку'),
        ('approved', 'Принят')
    ]
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return self.homework.title
