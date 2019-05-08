from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User


def login_view(request):
    if request.user.is_authenticated:
        redirect_url = reverse('user_list')
        return redirect(redirect_url)
    else:
        return render(request, 'index.html')


class UserListView(ListView):
    template_name = 'administration/user_list.html'
    model = User

    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False)
