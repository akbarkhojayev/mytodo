from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request,'register.html')

    def post(self, request):
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1')
            )
            login(request, user)
            return redirect('home')
        return redirect('register')