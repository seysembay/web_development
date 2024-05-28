from django.urls import path
from .views import CourseListCreate, CourseRunListCreate, LessonListCreate, EnrollmentListCreate, HomeworkListCreate, \
    CourseDetailView, UserEnrolledCoursesListView, UserEnrolledCourseRunView, LessonListView, HomeworkListView, \
    HomeworkSubmissionView

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('owncourses/', UserEnrolledCoursesListView.as_view(), name='own-courses'),
    path('owncourserun/<int:pk>/', UserEnrolledCourseRunView.as_view(), name='own-courserun'),
    path('getLessons/', LessonListView.as_view(), name='own-lessons'),
    path('courseruns/', CourseRunListCreate.as_view(), name='courserun-list'),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list'),
    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list'),
    path('homeworks/', HomeworkListCreate.as_view(), name='homework-list'),
    path('ownhomeworks/', HomeworkListView.as_view(), name='own-homework-list'),
    path('hw-submission/<int:pk>/', HomeworkSubmissionView.as_view(), name='hw-submission'),
]
