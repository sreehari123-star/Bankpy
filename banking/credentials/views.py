from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.models import Bank


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist.')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not matching.')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bank')
        else:
            messages.info(request,'Invalid User.')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def bank(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        address = request.POST['address']
        banks = Bank(name=name,dob=dob,email=email,address=address)
        banks.save()
        messages.info(request,'successful')
        return redirect('bank')
    return render(request,'bank.html')
