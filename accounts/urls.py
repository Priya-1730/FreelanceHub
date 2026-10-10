from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'client/dashboard/',
        views.client_dashboard,
        name='client_dashboard'
    ),

    path(
        'freelancer/dashboard/',
        views.freelancer_dashboard,
        name='freelancer_dashboard'
    ),
    path(
    'profile/edit/',
    views.edit_profile,
    name='edit_profile'
),
]