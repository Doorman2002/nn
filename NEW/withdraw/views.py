from django.shortcuts import render

# Create your views here.
def withdraw(request):
    return render(request,"withdraw.html")