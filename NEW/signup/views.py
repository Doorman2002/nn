from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from .models import Signup

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")

        # ✅ 1. Check password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        # ✅ 2. Check email already used
        if Signup.objects.filter(email=email).exists():
            messages.error(request, "This email has already been registered.")
            return render(request, "signup.html")

        # ✅ 3. Save new user safely
        try:
            Signup.objects.create(
                name=name,
                email=email,
                password=make_password(password)
            )
            messages.success(request, "Account created successfully! Please log in below.")
            
            # ✅ 4. Instead of redirect, just render login page
            return render(request, "login.html")

        except IntegrityError:
            messages.error(request, "Something went wrong. Try again.")
            return render(request, "signup.html")

    # ✅ 5. Default: show signup form
    return render(request, "signup.html")
