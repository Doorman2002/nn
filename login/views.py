from django.shortcuts import render, redirect
from signup.models import Signup
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Signup.objects.filter(email=email).first()  

        if user:
            if check_password(password, user.password):
                # Save user info in session
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                request.session["user_balance"] = user.balance
                context={"name":user.name, "balance":user.balance}

                return render(request,"dashboard.html",context)  # redirect to the dashboard view
            else:
                messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "Email not registered.")

    return render(request, "login.html")
