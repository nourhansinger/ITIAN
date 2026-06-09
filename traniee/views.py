from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def listTrainees(request):
        return HttpResponse("List of Trainees")   

def addTrainee(request):
        return HttpResponse("Add Trainee")

def updateTrainee(request, id):
        return HttpResponse(f"Update Trainee with ID: {id}")

def deleteTrainee(request, id): 
        return HttpResponse(f"Delete Trainee with ID: {id}") 
    
def getTraineeById(request, id):
        return HttpResponse(f"Get Trainee with ID: {id}")

    