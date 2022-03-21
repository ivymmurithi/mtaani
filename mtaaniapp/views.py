from django.shortcuts import redirect, render
from .forms import RegisterForm, PostForm, MtaaniForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.contrib import messages

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
    mtaani_objects = Neighbourhood.objects.all()
    return render(request, "index.html", {'mtaanis':mtaani_objects})

@login_required
def profile(request):
    current_user = request.user
    profile_object = Profile.objects.all().filter(user=current_user.id)
    mtaani_form = MtaaniForm()
    return render(request, 'profile.html',{'profiles':profile_object,'mtaani_form':mtaani_form})

def profilemtaani(request, profile_id):
    if request.method == 'POST':
        mtaani = Profile.objects.get(pk=profile_id)
        mtaani_form = MtaaniForm(request.POST, instance=mtaani)
        if mtaani_form.is_valid():
            mtaani_form.save()
            return redirect('/profile/',{'mtaani_form':mtaani_form})
        else:
            mtaani_form = MtaaniForm()
    else:
         mtaani_form = MtaaniForm()
    return render(request, 'profile.html')

@login_required
def posts(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.cleaned_data['user_id'] = request.session['_auth_user_id']
            userposted = post_form.save()
            userposted.profile_user_id = request.session['_auth_user_id']
            userposted.save()
            return redirect('/posts/')
        else:
            post_form=PostForm()
    else:
        post_form = PostForm()
        post_object = Post.objects.all()
    return render(request, 'posts.html',{'posts':post_object, 'post_form':post_form})

@login_required
def business(request):
    business_object = Business.objects.all()
    return render(request, 'business.html', {'businesses':business_object})

@login_required
def business_results(request):
    if request.method == 'POST':
        if 'biz' in request.POST and request.POST['biz']:
            searched_biz = request.POST['biz']
            biz_objects = Business.objects.filter(neighbourhood__mtaani_name__icontains=searched_biz)
            return render(request, 'bizsearch.html',{'businesses':biz_objects})
        else:
            messages.error(request, "Business does not exist!")
    return render(request,'bizsearch.html')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')