from django.urls import path

from .views import login_view, UserListView, create_user, UserUpdate

urlpatterns = [
    path('', login_view),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', create_user, name='user_create'),
    path('users/edit/<int:pk>', UserUpdate.as_view(), name='user_edit'),
]
