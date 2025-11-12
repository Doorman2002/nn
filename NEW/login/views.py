from django.shortcuts import render
from signup.models import Signup
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Signup.objects.filter(email=email).first()  # 👈 use Signup model

        if user:
            name=user.name
            amount=user.balance
            if check_password(password, user.password):
                return render(request, "dashboard.html", {"name": name,"balance":amount})
            else:
                messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "Email not registered.")

        return render(request, "login.html")

    return render(request, "login.html")
