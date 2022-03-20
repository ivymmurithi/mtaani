from django.shortcuts import redirect, render
from .forms import RegisterForm, PostForm
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
def posts(request):
    if request.method == 'POST':
        username  = request.user.get_username()           
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('/posts/')
        else:
            post_form=PostForm()
    else:
        username  = request.user.get_username() 
        post_form = PostForm
        post_object = Post.objects.all()
    return render(request, 'posts.html',{'posts':post_object, 'post_form':post_form,'username':username})

@login_required
def business(request):
    business_object = Business.objects.all()
    return render(request, 'business.html', {'businesses':business_object})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')