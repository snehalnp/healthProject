from django import forms
from .models import HealthRecord
from .models import CalorieIntake
from .models import Activity


class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['date', 'weight', 'blood_pressure', 'heart_rate', 'steps', 'sleep_hours']



class CalorieIntakeForm(forms.ModelForm):
    class Meta:
        model = CalorieIntake
        fields = ['date', 'food', 'quantity']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['exercise', 'date', 'duration']

