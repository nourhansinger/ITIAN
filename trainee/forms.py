from django import forms
from .models import Trainee
from course.models import Course

class TraineeForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Trainee
        fields = ['name','courses']