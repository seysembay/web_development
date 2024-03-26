from rest_framework import generics
from .models import Course, CourseRun, Lesson, Enrollment, Homework
from .serializers import CourseSerializer, CourseRunSerializer, LessonSerializer, EnrollmentSerializer, \
    HomeworkSerializer


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRunListCreate(generics.ListCreateAPIView):
    queryset = CourseRun.objects.all()
    serializer_class = CourseRunSerializer


class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class EnrollmentListCreate(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class HomeworkListCreate(generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
