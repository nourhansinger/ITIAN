from django.urls import path
from . import views
from .views import TraineeCreateView, TraineeUpdateView

urlpatterns = [
    path('', views.listTrainees, name='trainee_list'),
    path('add/', TraineeCreateView.as_view(), name='trainee_add'),
    path('update/<int:id>/', TraineeUpdateView.as_view(), name='trainee_update'),
    path('delete/<int:id>/', views.deleteTrainee, name='trainee_delete'),
    path('getbyid/<int:id>/', views.getTraineeById, name='trainee_getbyid'),
]

