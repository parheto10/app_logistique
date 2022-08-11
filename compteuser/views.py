from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,"Utilisateur ou mot de passe incorrect.")
            
    return render(request, 'pages/login.html')


def deconnect(request):
    logout(request)
    return redirect('compteuser:login')
