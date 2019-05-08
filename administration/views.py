from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User
from .forms import UserForm


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


@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'administration/create_user.html', {'form': form})
