from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserForm, UserProfileForm


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("home")
        else:
            messages.error(request, "Your username or password is incorrect")
            return redirect("home")
    else:
        return render(request, "home.html", {})



@login_required
def Parking_and_profile_Management(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('Parking_and_profile_Management')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
        
    return render(request, "Parking_and_profile_Management.html", {
        'user_form': user_form, 'profile_form': profile_form
    })


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered successfully.")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form})



def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("home")