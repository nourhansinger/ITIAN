from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, TrackViewSet, TraineeViewSet, RegisterView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'trainees', TraineeViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
