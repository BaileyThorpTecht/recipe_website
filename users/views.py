from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created.")
            return redirect('user-login')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
