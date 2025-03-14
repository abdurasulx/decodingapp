from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usr, Savol

@login_required(login_url='login')
def home(request):
    user_data, created = Usr.objects.get_or_create(user=request.user)
    savollar = Savol.objects.all()
    return render(request, 'index.html', {"user_data": user_data, 'ques': savollar})

@login_required(login_url='login')
def seeque(request, slug):
    usr, created = Usr.objects.get_or_create(user=request.user)
    if usr.lvl < int(slug):
        return render(request, '404.html')
    
    savol = get_object_or_404(Savol, id=slug)
    ans = request.POST.get('answer', '')

    correct = '2' if ans and ans == savol.answer else '3' if ans else '1'

    if correct == '2' and usr.lvl == savol.id:
        usr.lvl += 1
        usr.save()

    return render(request, 'post.html', {'savol': savol, 'a': ans, 'correct': correct})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Login yoki parol noto‘g‘ri!"})

    return render(request, 'login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {"error": "Bu username allaqachon band!"})
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
