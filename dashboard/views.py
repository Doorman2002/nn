from django.shortcuts import render
from signup.models import Signup
from login.models import Login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def dashboard(request):
    # email=Login.objects.filter(email=email).first()
    # bal=Login.objects.get(balance=balance).first()
    # user=Signup.objects.get(email=email)
    name="NEW"
    balance=0.00
    context={"name":name,"balance":balance}
    return render(request,"dashboard.html",context)
