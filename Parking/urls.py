
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name= "home"
        ),
    # path('Login/', views.login_user, name= "login"),
    path(
        'Logout/',
        views.logout_user,
        name= "logout"
        ),
    path(
        'Register/',
        views.register_user, 
        name= "register"
        ),
     path(
        'Parking_and_profile_Management ',
        views.Parking_and_profile_Management,
        name= "Parking_and_profile_Management"
        ),
    
    
]
