from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            redirect('LoginForm')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })
    
def login(request):
    # ......................................................
    if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # log the user in
                user = form.get_user()
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def home(request):
    # return redirect()
    return render(request, 'accounts\home.html')

# def logout(reque)