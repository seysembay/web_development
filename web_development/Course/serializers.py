from rest_framework import serializers

from User.models import CustomUser
from .models import Course, CourseRun, Lesson, Enrollment, Homework, HomeworkSubmission


class CourseRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRun
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    courseruns = CourseRunSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'username', 'email', 'role']

    def get_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"


class LessonSerializer(serializers.ModelSerializer):
    homeworks = HomeworkSerializer()
    teacher = CustomUserSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'published_date', 'start', 'course', 'teacher', 'homeworks']


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer()

    class Meta:
        model = HomeworkSubmission
        fields = ['id', 'student', 'submission_date', 'content', 'status']
