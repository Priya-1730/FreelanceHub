from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout

from .models import User


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )

        login(request, user)

        if role == 'CLIENT':
            return redirect('client_dashboard')
        else:
            return redirect('freelancer_dashboard')

    return render(
        request,
        'accounts/register.html'
    )


def client_dashboard(request):

    return render(
        request,
        'accounts/client_dashboard.html'
    )


def freelancer_dashboard(request):

    return render(
        request,
        'accounts/freelancer_dashboard.html'
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'CLIENT':
                return redirect('client_dashboard')
            else:
                return redirect('freelancer_dashboard')

    return render(
        request,
        'accounts/login.html'
    )


def user_logout(request):

    logout(request)

    return redirect('login')


def home(request):

    return render(
        request,
        'home.html'
    )


@login_required
def profile(request):

    return render(
        request,
        'accounts/profile.html'
    )


@login_required
def edit_profile(request):

    if request.method == 'POST':

        request.user.email = request.POST['email']

        request.user.bio = request.POST['bio']

        if request.user.role == 'FREELANCER':
            request.user.skills = request.POST['skills']

        request.user.save()

        return redirect('profile')

    return render(
        request,
        'accounts/edit_profile.html'
    )