from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('/login/', {'register_form':register_form})
    else:
        register_form = RegisterForm()
    return render(request, 'registration/register.html', {'register_form':register_form})

def index(request):
    return render(request, "index.html")

@login_required
def profile(request):
    current_user = request.user
    profile_object = Profile.objects.all().filter(user=current_user.id)
    return render(request, 'profile.html',{'profiles':profile_object})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')