from django.shortcuts import render,redirect
from main.models import Category
from django.contrib.auth import login,authenticate, logout
from .forms import User_from
from django.contrib.auth.models import User
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username,password=password)

        if user:
            login(request, user)
            return redirect('home')




    category=Category.objects.all()
    

    context={
        'categories':category,
        'title':'Sign In'
    }
    return render(
        request=request,
        template_name='user/login.html',
        context=context
    )


def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = User_from(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')

    category=Category.objects.all()
    context={
        'categories': category,
        'title': 'Sign Up',
        'form': User_from
    }
    return render(request, 'user/register.html', context)
