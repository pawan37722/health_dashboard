from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import HealthEntryForm
from .models import HealthEntry
from django.utils.dateformat import DateFormat

def index(request):
    return render(request, 'tracker/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'tracker/dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = HealthEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = HealthEntryForm()

    entries = HealthEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/dashboard.html', {
        'form': form,
        'entries': entries
    })
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = HealthEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = HealthEntryForm()

    entries = HealthEntry.objects.filter(user=request.user).order_by('date')

    # Prepare chart data
    dates = [DateFormat(e.date).format('M d') for e in entries]
    weights = [e.weight for e in entries]
    sleep_hours = [e.sleep_hours for e in entries]

    context = {
        'form': form,
        'entries': entries,
        'dates': dates,
        'weights': weights,
        'sleep_hours': sleep_hours
    }

    return render(request, 'tracker/dashboard.html', context)

# Create your views here.
