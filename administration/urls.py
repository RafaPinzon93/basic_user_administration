from django.urls import path

from .views import login_view, logout_view, UserListView, create_user, UserUpdate, UserDetail, UserDelete

urlpatterns = [
    path('', login_view, name='index'),
    path('logout/', logout_view, name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', create_user, name='user_create'),
    path('users/edit/<int:pk>', UserUpdate.as_view(), name='user_edit'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('users/delete/<int:pk>', UserDelete.as_view(), name='user_delete'),
]
