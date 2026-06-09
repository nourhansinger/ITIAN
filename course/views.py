from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

class CourseCreateView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'course/add.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        return render(request, 'course/add.html', {'form': form})

class CourseUpdateView(View):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        form = CourseForm(instance=course)
        return render(request, 'course/update.html', {'form': form})

    def post(self, request, id):
        course = get_object_or_404(Course, id=id)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        return render(request, 'course/update.html', {'form': form})

def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course/detail.html', {'course': course})