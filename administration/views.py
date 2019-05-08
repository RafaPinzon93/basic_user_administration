from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
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
    return render(request, 'administration/user_form.html', {'form': form, 'title': "Create User"})


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "administration/user_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update User"
        return context

    def get_success_url(self):
        return reverse('user_list')
