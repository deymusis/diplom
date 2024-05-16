from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, LinksForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Link


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан!')
            return redirect('user')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)


@login_required
def link(request):
    if request.method == "POST":
        form = LinksForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('links')
    else:
        form = LinksForm()

    links = Link.objects.filter(user=request.user)

    data = {
        'title': 'Создание сокращений',
        'form': form,
        'links': links
    }
    return render(request, 'users/links.html', data)


def redirect_url_view(request, slug):
    link = Link.objects.filter(link2=slug).first()
    return redirect(link.link1)