from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
 

def signup(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email taken')
                 return redirect('signup')
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password1)
            user.save()
            messages.info(request,'user created')
            return redirect('signin')

        else:
             messages.info(request,'not match')
             return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')    


