from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserListCreate.as_view(), name="user-list-create"),
    path("users/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="user-retrieve-update-destroy"),
]