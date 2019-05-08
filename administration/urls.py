from django.urls import path

from .views import login_view, UserListView, create_user

urlpatterns = [
    path('', login_view),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/create', create_user, name='user_create'),
]
