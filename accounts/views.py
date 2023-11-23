from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        user =  request.POST.get('username')
        password =  request.POST.get('password')

        userVerify = auth.authenticate(request, username=user, password=password)
        print(userVerify)
        if userVerify == None:
            messages.info(request, "usuário ou senha invalido(s)")
            return redirect('login')
        else:
            auth.login(request,userVerify)
            return redirect('home')
    
    else:
        return render(request, 'pages/login.html')
    

def register(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('rPassword')
        User.objects.create_user(username=user,
                                 email=email,
                                 password=password)
    else:
        return render(request, 'pages/register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

