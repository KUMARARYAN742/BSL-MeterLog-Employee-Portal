from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import MeterReading
from .forms import MeterReadingForm
from .forms import CustomUserCreationForm  # Assuming you have a custom form

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))  # Ensure 'dashboard' is a valid URL name
        else:
            return render(request, 'auth/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'auth/register.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('dashboard'))  # Redirect to the dashboard or any success page
        else:
            return render(request, 'auth/login.html', {'form': form})  # Re-render the form with errors
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def dashboard_view(request):
    user = request.user
    meter_readings = MeterReading.objects.filter(user=user)

    if request.method == 'POST':
        form = MeterReadingForm(request.POST, request.FILES)
        if form.is_valid():
            meter_reading = form.save(commit=False)
            meter_reading.user = user
            meter_reading.save()
            return redirect('dashboard')
    else:
        form = MeterReadingForm()

    context = {
        'username': user.username,
        'meter_readings': meter_readings,
        'form': form,
    }
    return render(request, 'auth/dashboard.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')

def HomePage(request):
    return render(request, 'home/home.html')