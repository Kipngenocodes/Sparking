
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    # path('Login/', views.login_user, name= "login"),
    path('Logout/', views.logout_user, name= "logout"),
    
]
