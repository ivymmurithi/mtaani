from django.shortcuts import redirect, render
from .forms import RegisterForm, PostForm, MtaaniForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.contrib import messages
from django.contrib.postgres.search import SearchVector

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
        current_user = request.user
        profile = Profile.objects.get(user=current_user)
        if profile.neighbourhood:
            post_object = Post.objects.filter(neighbourhood=profile.neighbourhood)
        else:
            post_object = Post.objects.all()
    return render(request, 'posts.html',{'posts':post_object, 'post_form':post_form})

@login_required
def business(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if profile.neighbourhood:
        business_object = Business.objects.filter(neighbourhood=profile.neighbourhood)
    else:
        business_object = Business.objects.all()
    return render(request, 'business.html', {'businesses':business_object})

@login_required
def business_results(request):
    if request.method == 'POST':
        search_vector = SearchVector("business_name") + SearchVector("business_description") + SearchVector("business_email")
        search_term = request.POST['biz']
        businesses = Business.objects.annotate(search=search_vector).filter(search=search_term)
        return render(request,'bizsearch.html', {'businesses':businesses})
    return render(request,'bizsearch.html')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')