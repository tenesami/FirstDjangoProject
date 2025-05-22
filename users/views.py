
from django.shortcuts import render, redirect
from django.contrib import  messages
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for You are now able to log in')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('login')
# def register(request):
    # if request.method == 'POST':
    #     # Handle the registration logic here
    #     pass
    # return render(request, 'users/register.html')