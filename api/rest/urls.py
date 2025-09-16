from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view(), name="users"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
]