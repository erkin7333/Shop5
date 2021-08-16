from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, Login_User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User


class UserRegister(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request):
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            del data['confirm']
            user = User(**data)
            user.set_password(data['password'])
            user.save()
            return redirect('accounts:login')
        return render(request, 'accounts/register.html', {"form": form})


def user_login(request):
    form = Login_User()
    if request.POST:
        form = Login_User(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main:index')
            form.add_error('password', "Username va/yoki parol noto'g'ri. ")

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main:index')
