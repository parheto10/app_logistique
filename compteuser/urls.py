from django.urls import path

from compteuser.views import deconnect, loginView 

app_name="compteuser"

urlpatterns = [
    path('',loginView, name="login"),
    path('deconnect/',deconnect, name="deconnect")
]
