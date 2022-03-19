from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm()
        if register_form.is_valid():
            register_form.save()
        return redirect('/')
    else:
        register_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':register_form})

def index(request):
    return render(request, "index.html")