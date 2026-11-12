from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


# Create your views here.
def signup_view(request):
   if request.method == "POST":
       username = request.POST.get("username")
       email = request.POST.get("email")
       password1 = request.POST.get("password1")
       password2 = request.POST.get("password2")


       # Check empty fields
       if not username or not email or not password1:
           messages.error(request, "All fields are required!")
           return redirect("register")


       if password1 != password2:
           messages.error(request, "Passwords do not match!")
           return redirect("register")
       if User.objects.filter(username=username).exists():
           messages.error(request, "Username already exists!")
           return redirect("register")


           # Email exists check (optional but good)
       if User.objects.filter(email=email).exists():
           messages.error(request, "Email already exists!")
           return redirect("register")


       user = User.objects.create_user(username=username, email=email, password=password1)


       messages.success(request, "Account created successfully! Please login.")
       return redirect("login")
   return render(request, "signup.html")

@login_required
@never_cache
def dashboard_view(request):
    return render(request, "farmer_dashboard.html")