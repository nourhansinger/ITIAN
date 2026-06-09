from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from .forms import TraineeForm


def listTrainees(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def addTrainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/trainee_add.html', {'form': form})


def updateTrainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/trainee_update.html', {'form': form})

def deleteTrainee(request, id): 
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/delete_trainee.html', {'trainee': trainee})

def getTraineeById(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/trainee_details.html', {'trainee': trainee})
    
   
