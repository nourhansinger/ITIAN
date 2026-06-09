from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import TraineeForm


def listTrainees(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

class TraineeCreateView(View):
    def get(self, request):
        form = TraineeForm()
        return render(request, 'trainee/trainee_add.html', {'form': form})

    def post(self, request):
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
        return render(request, 'trainee/trainee_add.html', {'form': form})


class TraineeUpdateView(View):
    def get(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        form = TraineeForm(instance=trainee)
        return render(request, 'trainee/trainee_update.html', {'form': form})

    def post(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
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

