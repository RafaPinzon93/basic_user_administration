from django.urls import path

from .views import login_view, UserListView

urlpatterns = [
    path('', login_view),
    path('users', UserListView.as_view(), name='user_list'),
]
