from django import forms
from .models import Meeting
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

def validate_date(value):
    try:
        datetime.datetime.strptime(value, '%Y%m%d')
    except ValueError:
        raise ValidationError("Invalid date format. Use YYYYMMDD.")

def validate_time(value):
    try:
        datetime.datetime.strptime(value, '%H%M%S')
    except ValueError:
        raise ValidationError("Invalid time format. Use HHMMSS.")

class MeetingForm(forms.ModelForm):
    meeting_date = forms.CharField(validators=[validate_date], widget=forms.TextInput(attrs={'placeholder': 'YYYYMMDD'}))
    start_time = forms.CharField(validators=[validate_time], widget=forms.TextInput(attrs={'placeholder': 'HHMMSS'}))
    duration = forms.ChoiceField(choices=[(str(i/2), f"{i/2} hours") for i in range(1, 21)], widget=forms.Select())
    meeting_room = forms.ChoiceField(choices=[(f"RM {i}", f"RM {i}") for i in range(1, 11)], widget=forms.Select())

    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'user': forms.TextInput(attrs={'readonly': 'readonly'}),
        }