from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    # Checking if you are logging in.
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authentication of the person trying to login.
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





def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
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