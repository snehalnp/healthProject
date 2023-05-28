from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthRecord
from .forms import HealthRecordForm
from .models import Food, CalorieIntake
from .forms import CalorieIntakeForm
from .models import Exercise, Activity
from .forms import ActivityForm
from .models import HealthRecord
from .forms import HealthRecordForm



def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # to check if user already exists
        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, "Account does not exists")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.warning(request, "Invalid Password")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('/')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # to check if user already exists
        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, "Username already exists")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if password == confirm_password:
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            return redirect('/')
        else:
            messages.warning(request, "Your Password does not match")

    return render(request,'register.html')


@login_required
def health_record(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('health_record')
    else:
        form = HealthRecordForm()

    records = HealthRecord.objects.filter(user=request.user).order_by('-date')
    context = {'form': form, 'records': records}
    return render(request, 'health_record.html', context)



@login_required
def calorie_intake(request):
    if request.method == 'POST':
        form = CalorieIntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user
            intake.save()
            return redirect('calorie_intake')
    else:
        form = CalorieIntakeForm()

    intake_records = CalorieIntake.objects.filter(user=request.user).order_by('-date')
    context = {'form': form, 'intake_records': intake_records}
    return render(request, 'calorie_intake.html', context)


@login_required
def activity_log(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activity_log')
    else:
        form = ActivityForm()

    activity_records = Activity.objects.filter(user=request.user).order_by('-date')
    context = {'form': form, 'activity_records': activity_records}
    return render(request, 'activity_log.html', context)
