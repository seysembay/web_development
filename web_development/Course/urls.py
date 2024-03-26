from django.urls import path
from .views import CourseListCreate, CourseRunListCreate, LessonListCreate, EnrollmentListCreate, HomeworkListCreate

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list'),
    path('courseruns/', CourseRunListCreate.as_view(), name='courserun-list'),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list'),
    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list'),
    path('homeworks/', HomeworkListCreate.as_view(), name='homework-list'),
]
