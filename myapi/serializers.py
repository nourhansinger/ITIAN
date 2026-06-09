from rest_framework import serializers
from django.contrib.auth.models import User
from course.models import Course
from track.models import Track
from trainee.models import Trainee


class CourseSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Course
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
   
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
