from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request):
    if request.user.is_authenticated:
        redirect_url = reverse('user_list')
        return redirect(redirect_url)
    else:
        return render(request, 'index.html')


@login_required
def user_list(request):
    return render(request, 'administration/user_list.html')
