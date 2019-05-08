from django.urls import path

from .views import login_view, user_list

urlpatterns = [
    path('', login_view),
    path('users', user_list, name='user_list'),
]
