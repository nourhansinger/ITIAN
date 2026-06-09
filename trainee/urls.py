from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('',listTrainees, name='trainee_list'),
    path('add/',addTrainee, name='trainee_add'),
    path('update/<int:id>/',updateTrainee, name='trainee_update'),
    path('delete/<int:id>/',deleteTrainee, name='trainee_delete'),
    path('getbyid/<int:id>/', getTraineeById, name='trainee_getbyid'),
]
