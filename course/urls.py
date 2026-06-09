from django.urls import path
from . import views
from .views import CourseCreateView, CourseUpdateView

urlpatterns = [
    path('', views.course_list, name='course_list_base'),
    path('list/', views.course_list, name='course_list'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('update/<int:id>/', CourseUpdateView.as_view(), name='course_update'),
    path('delete/<int:id>/', views.course_delete, name='course_delete'),
    path('detail/<int:id>/', views.course_detail, name='course_detail'),
]