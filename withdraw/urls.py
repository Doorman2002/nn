from django.urls import path

from . import views

urlpatterns = [
    path("",views.withdraw,name="withdraw")
]
