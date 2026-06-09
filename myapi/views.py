from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from course.models import Course
from track.models import Track
from trainee.models import Trainee
from .serializers import (CourseSerializer,TrackSerializer,TraineeSerializer,RegisterSerializer,)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
