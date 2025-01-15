from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm, MeetingForm
from .models import Meeting
from django.contrib import messages
import datetime

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('welcome')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def welcome(request):
    if not request.user.is_authenticated:
        return redirect('index')
    meetings = Meeting.objects.all()
    return render(request, 'welcome.html', {'meetings': meetings})

def reserve_meeting(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            # Check for overlapping meetings
            meeting = form.save(commit=False)
            overlaps = Meeting.objects.filter(
                meeting_room=meeting.meeting_room,
                meeting_date=meeting.meeting_date,
                start_time__lt=(datetime.datetime.combine(meeting.meeting_date, meeting.start_time) + meeting.duration).time(),
                start_time__gt=meeting.start_time
            )
            if overlaps.exists():
                messages.error(request, 'Meeting overlap detected. Please modify the details.')
                return render(request, 'reservation.html', {'form': form})
            meeting.user = request.user
            meeting.save()
            messages.success(request, 'Meeting reserved successfully!')
            return redirect('welcome')
        else:
            messages.error(request, 'Failed to reserve meeting. Please fill all fields correctly.')
    else:
        form = MeetingForm()
    return render(request, 'reservation.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')