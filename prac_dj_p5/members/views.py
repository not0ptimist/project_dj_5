from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


# Create your views here.
# Login User
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('base')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an Error logining, try again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

# Logout User
def logout_user(request):
    logout(request)
    messages.success(request, ('You were logout'))
    return redirect('base')

# Register User
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Sucesfull")
            return redirect('base')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
        })