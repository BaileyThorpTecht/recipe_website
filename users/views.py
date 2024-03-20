from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.isvalid():
            form.save()
            
            
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created.")
            return redirect('recipe-login')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
            
@login_required()
def profile(request):
    return render(request, 'users/profile.html')

