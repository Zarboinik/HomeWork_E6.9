from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import GroupForm, UserProfileForm
from .models import Group, UserProfile


def index(request):
    groups = Group.objects.all()
    create_group_url = reverse('chat:create_group')
    users = User.objects.all()  # Получаем всех пользователей из таблицы auth_user

    return render(request, "chat/index.html", {"groups": groups,
                                               "create_group_url": create_group_url,
                                               'users': users
                                               })


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:index')  # Перенаправляем на страницу index после создания группы
    else:
        form = GroupForm()
    return render(request, 'chat/create_group.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:index')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'chat/edit_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
