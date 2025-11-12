from django.urls import path
from . import views

urlpatterns = [
    path("",views.withdraw_process,name="withdraw_processing")
]
