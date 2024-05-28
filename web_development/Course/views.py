from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, CourseRun, Lesson, Enrollment, Homework, HomeworkSubmission
from .serializers import CourseSerializer, CourseRunSerializer, LessonSerializer, EnrollmentSerializer, \
    HomeworkSerializer, HomeworkSubmissionSerializer


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


class CourseDetailView(APIView):
    def get_object(self, pk):
        return Course.objects.get(pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        c_serializer = CourseSerializer(course)
        courses = CourseRun.objects.filter(course=pk)
        cr_serializer = CourseRunSerializer(courses, many=True)
        return Response({
            'course': c_serializer.data,
            'courseruns': cr_serializer.data
        })


class UserEnrolledCoursesListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Course.objects.filter(courserun__enrollment__student_id=user_id)


class UserEnrolledCourseRunView(generics.RetrieveAPIView):
    serializer_class = CourseRunSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return CourseRun.objects.filter(enrollment__student_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.first()


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        course_run_id = self.request.GET.get('course_run_id')
        return Lesson.objects.filter(course__id=course_run_id)


class HomeworkListView(ListAPIView):
    serializer_class = HomeworkSerializer

    def get_queryset(self):
        course_run_id = self.request.GET.get('course_run_id')
        return Homework.objects.filter(lesson__course_id=course_run_id)


class HomeworkSubmissionView(ListAPIView):
    serializer_class = HomeworkSubmissionSerializer

    def get_queryset(self):
        current_student = self.request.user
        homework_id = self.kwargs['pk']
        return HomeworkSubmission.objects.filter(student=current_student, homework_id=homework_id).order_by('id')
