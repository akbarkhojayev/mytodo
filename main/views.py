from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
            context = {
                'tasks': tasks,
                'STATUS_CHOICES': Task.STATUS_CHOICES,
            }
            return render(request,'index.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            deadline = request.POST.get('deadline')
            if deadline == '':
                deadline = None
            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                deadline=deadline,
                status=request.POST.get('status'),
                owner=request.user
            )
            return redirect('home')
        return redirect('login')

class EditView(View):
    def get(self, request , pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, pk=pk)
            task = get_object_or_404(Task, pk=pk)
            context = {
                'task': task,
                'STATUS_CHOICES': Task.STATUS_CHOICES,
            }

            return render(request,'edit.html',context)
        return redirect('login')

    def post(self, request , pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, pk=pk)
            Task.objects.filter(pk=pk).update(
                title = request.POST.get('title'),
                description = request.POST.get('description'),
                status = request.POST.get('status'),
            )
            return redirect('home')
        return redirect('login')

class DeleteView(View):
    def get(self, request , pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, pk=pk)
            task.delete()
            return redirect('home')
        return redirect('login')
